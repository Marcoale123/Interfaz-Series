import pandas as pd
import networkx as nx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from fastapi.responses import FileResponse
from typing import List, Dict
import matplotlib.pyplot as plt
import os
=======
from typing import List, Dict
>>>>>>> 758552ab891a91e87d0462964a58e529300be7c5

app = FastAPI()

# Configurar el middleware CORS para permitir todas las solicitudes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Leer el archivo CSV una sola vez al inicio de la aplicación
<<<<<<< HEAD
df = pd.read_csv('series_de_peliculas5.csv', on_bad_lines='skip')
=======
df = pd.read_csv('series_de_peliculas.csv')
>>>>>>> 758552ab891a91e87d0462964a58e529300be7c5

# Modificar el formato de los nombres en el DataFrame
df['nombre_modificado'] = df['name'].str.replace(' ', '_').str.lower()  # Reemplazar espacios por guiones bajos y convertir a minúsculas

# Crear un diccionario para almacenar el grafo y el MST
graph_data = {
    'nodes': {},
    'edges': [],
    'mst': None
}

# Llenar el diccionario con los datos del grafo
for index, row in df.iterrows():
    graph_data['nodes'][str(row['movie_id'])] = {
        'nombre_modificado': row['nombre_modificado'],
        'gender': row['genre'],
        'description': row['description'], 
        'image_url': row['image_url']       
    }
    graph_data['edges'].append((str(row['movie_id']), row['nombre_modificado'], {'genre': row['genre'], 'weight': 1}))

# Crear el grafo con NetworkX y calcular el MST
G = nx.Graph()
G.add_nodes_from(graph_data['nodes'].keys())
G.add_edges_from(graph_data['edges'])
graph_data['mst'] = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Funciones de la API
@app.get("/mst/id/{movie_id}", response_model=List[Dict])
def get_mst_by_id(movie_id: str):
    if movie_id not in graph_data['nodes']:
        raise HTTPException(status_code=404, detail="Movie ID not found")

    mst_edges = []
    for u, v, d in graph_data['mst'].edges(data=True):
        if u == movie_id or v == movie_id:
            mst_edges.append({
                'source': u,
                'target': v,
                'weight': d['weight'],
                'genre': d['genre'],
                'description': graph_data['nodes'][u]['description'],  # Agregar descripción a la respuesta
                'image_url': graph_data['nodes'][u]['image_url']       # Agregar URL de imagen a la respuesta
            })

    return mst_edges

@app.get("/mst/name/{name}", response_model=List[Dict])
def get_mst_by_name(name: str):
    name_modificado = name.replace(' ', '_').lower()  # Modificar el nombre ingresado por el usuario
    nodes = [n for n, d in graph_data['nodes'].items() if d['nombre_modificado'] == name_modificado]
    if not nodes:
        raise HTTPException(status_code=404, detail="Movie name not found")

    mst_edges = []
    for node in nodes:
        for u, v, d in graph_data['mst'].edges(data=True):
            if u == node or v == node:
                mst_edges.append({
                    'source': u,
                    'target': v,
                    'weight': d['weight'],
                    'genre': d['genre'],
                    'description': graph_data['nodes'][u]['description'],  # Agregar descripción a la respuesta
                    'image_url': graph_data['nodes'][u]['image_url']       # Agregar URL de imagen a la respuesta
                })

    return mst_edges

@app.get("/mst/genre/{genre}", response_model=List[Dict])
def get_mst_by_genre(genre: str):
    genre = genre.lower()  # Convertir el género a minúsculas para una comparación insensible a mayúsculas y minúsculas
    nodes = [n for n, d in graph_data['nodes'].items() if d['gender'].lower() == genre]
    if not nodes:
        raise HTTPException(status_code=404, detail="Genre not found")

    mst_edges = []
    for u, v, d in graph_data['mst'].edges(data=True):
        if u in nodes or v in nodes:
            mst_edges.append({
                'source': u,
                'target': v,
                'weight': d['weight'],
                'genre': d['genre'],
                'description': graph_data['nodes'][u]['description'],  # Agregar descripción a la respuesta
                'image_url': graph_data['nodes'][u]['image_url']       # Agregar URL de imagen a la respuesta
            })

    return mst_edges

<<<<<<< HEAD
# Endpoint para mostrar el grafo
@app.get("/graph")
def get_graph_image():
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, 'genre')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Guardar la imagen del grafo
    image_path = "graph.png"
    plt.savefig(image_path)
    plt.close()

    return FileResponse(image_path)

=======
>>>>>>> 758552ab891a91e87d0462964a58e529300be7c5
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

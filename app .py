

import pandas as pd
import numpy as np
from faker import Faker
import random

# Inicializar Faker para generación de datos sintéticos
fake = Faker()

# Número de entradas
num_entries = 1500

# Generar datos sintéticos
data = {
    "movie_id": range(1, num_entries + 1),
    "Título": [fake.sentence(nb_words=4) for _ in range(num_entries)],
    "Puntuación": np.random.uniform(1, 10, num_entries).round(1),
    "Géneros": [', '.join(fake.words(nb=random.randint(1, 3), ext_word_list=['Drama', 'Comedia', 'Ciencia Ficción', 'Acción', 'Terror', 'Documental', 'Romance', 'Animación', 'Aventura', 'Fantasía'])) for _ in range(num_entries)],
    "Sinopsis": [fake.text(max_nb_chars=200) for _ in range(num_entries)],
    "Tipo de transmisión": [random.choice(['Streaming', 'Cine', 'Televisión']) for _ in range(num_entries)],
    "Fecha de estreno": [fake.date_this_century() for _ in range(num_entries)],
    "Estado": [random.choice(['En emisión', 'Finalizada']) for _ in range(num_entries)],
    "Productores": [fake.company() for _ in range(num_entries)],
    "Licenciantes": [fake.company() for _ in range(num_entries)],
    "Estudios": [fake.company() for _ in range(num_entries)],
    "Fuente": [random.choice(['Original', 'Adaptación', 'Basada en un libro', 'Basada en hechos reales']) for _ in range(num_entries)],
    "Duración": [random.randint(60, 180) for _ in range(num_entries)],
    "Clasificación": [random.choice(['G', 'PG', 'PG-13', 'R', 'NC-17']) for _ in range(num_entries)],
    "Rango": np.random.uniform(1, 10, num_entries).round(1),
    "Popularidad": np.random.uniform(1, 100, num_entries).round(1),
    "Favoritos": [random.randint(1, 10000) for _ in range(num_entries)],
    "Puntuado por": [random.randint(1, 10000) for _ in range(num_entries)],
    "Miembros": [random.randint(1, 10000) for _ in range(num_entries)],
    "URL de la película": [fake.url() for _ in range(num_entries)],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('series_de_peliculas.csv', index=False)

print("CSV generado con éxito.")
import os
from dotenv import load_dotenv

# Definir la ruta base correctamente
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ENV_PATH = os.path.join(BASE_DIR, ".env")

print(f"Intentando cargar .env desde: {ENV_PATH}")  # Depuración

# Cargar el archivo .env
load_dotenv(ENV_PATH)

# Verificar si la variable se cargó correctamente
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("⚠️ ERROR: La variable DATABASE_URL no está definida en .env")

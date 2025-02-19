import redis
import os

# Obtiene la URL desde el archivo .env
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Conecta a Redis
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

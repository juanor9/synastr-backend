from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schemas.graphql import schema
from app.websockets.messaging import websocket_router

app = FastAPI()

# GraphQL
app.include_router(GraphQLRouter(schema), prefix="/graphql")

# WebSockets
app.include_router(websocket_router)

# JWT and OAuth2 routes
# ... (importar y agregar rutas de autenticación)
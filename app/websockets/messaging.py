from fastapi import APIRouter, WebSocket

websocket_router = APIRouter()

@websocket_router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    await websocket.send_text(f"Conexión establecida para el usuario {user_id}")
    
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Mensaje recibido: {data}")

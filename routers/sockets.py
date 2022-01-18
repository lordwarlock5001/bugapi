from fastapi import FastAPI,WebSocket,APIRouter

sockets=APIRouter(
    tags=["WS"],
    prefix="/ws"
)

@sockets.websocket("/text")
async def wst(websocket:WebSocket):
    print("here")
    await websocket.accept()
    while True:
        await websocket.send_text("Hello")
        break

@sockets.post("/test")
def test():
    pass
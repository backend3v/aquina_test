import asyncio
import websockets
from infraestructure.services.events import Event_Service





def get_data():
    return Event_Service().get()
async def websocket_server(websocket, path):
    while True:
        result = get_data()
        await websocket.send(f"Response: {result}")

start_server = websockets.serve(websocket_server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
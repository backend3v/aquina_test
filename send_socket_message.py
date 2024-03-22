import asyncio
import websockets

async def enviar_peticion():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send('get')
        respuesta = await websocket.recv()
        print(respuesta)
        
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(enviar_peticion())
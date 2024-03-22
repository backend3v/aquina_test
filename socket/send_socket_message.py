import asyncio
import websockets

async def enviar_peticion():
    async with websockets.connect('ws://localhost:8765') as websocket:
        # Enviar un mensaje al servidor
        await websocket.send('get')
        # Recibir la respuesta del servidor
        respuesta = await websocket.recv()
        print(f"Respuesta recibida del servidor: {respuesta}")
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(enviar_peticion())
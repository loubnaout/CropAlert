import asyncio
import websockets
from websockets.protocol import State

connected = {}

async def handler(websocket):
    username = await websocket.recv()
    connected[username] = websocket
    print(f"{username} connected.")

    try:
        async for message in websocket:
            print(f"Received from {username}: {message}")
            for user, ws in connected.items():
                if ws != websocket and ws.state == State.OPEN:
                    await ws.send(message)
    except websockets.ConnectionClosed:
        print(f"{username} disconnected.")
        del connected[username]

async def main():
    async with websockets.serve(handler, "localhost", 8767):
        print("WebSocket server running on ws://localhost:8767")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
from flask import Flask, render_template, session, copy_current_request_context
import asyncio
from websockets import serve



async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'





async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "127.0.0.1", 8765,ping_interval=None):
        await asyncio.Future()


asyncio.run(main())
if __name__ == '__main__':
    app.run( debug=True)
    
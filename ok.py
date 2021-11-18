from flask import Flask, render_template, session, copy_current_request_context
import asyncio
from websockets import serve



async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/test')
def test():
  return 'ok'


ola = ["{'state':false, 'component':25}", "{'state':true, 'component':26}", "{'state':false, 'component':27}"]
async def echo(websocket, path):
    while True:
      #  async for message in websocket:
      for i in ola:
        await websocket.send(i)
        await asyncio.sleep(1)

async def main():
    async with serve(echo, "localhost", 8766,ping_interval=None):
        await asyncio.Future()


asyncio.run(main())
if __name__ == '__main__':
    app.run( debug=True)
    

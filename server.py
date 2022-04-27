import asyncio
import json
from random import randint

import websockets


# create handler for each connection

async def handler(websocket, path):
    i = 0
    while True:
        i += 1
        jsonResult = json.dumps({"a": i, "b": randint(0, 2 ^ 32)})
        await websocket.send(jsonResult)


start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()

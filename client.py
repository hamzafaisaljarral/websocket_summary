import asyncio
import json

import websockets

from summary import oneminsummary

b = []


async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        i=0
        while True:
            i += 1
            response = await websocket.recv()
            data = json.loads(response)
            b.append(data["b"])
            if i == 100:
                oneminsummary(b)
                i = 0
                b.clear()


try:
    asyncio.get_event_loop().run_until_complete(test())
except Exception as e:
    asyncio.get_event_loop().close()




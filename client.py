import asyncio
import json

import websockets

b = []


async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            b.append(data["b"])

try:
    asyncio.get_event_loop().run_until_complete(test())
except Exception as e:
    asyncio.get_event_loop().close()


def oneminsummary():
    struct = {}
    struct["max"] = max(b)
    # find the min in b
    struct["min"] = min(b)
    # find the first in b
    struct["first"] = b[0]
    # find the last in b
    struct["last"] = b[-1]
    # find the number of prime numbers
    prime_num = []
    for i in b:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            prime_num.append(i)
    struct["prime"] = prime_num

    even_num = []
    odd_num = []
    for num in b:

        # checking condition
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)

    struct["even_number"] = even_num
    struct["odd_number"] = odd_num

    return struct

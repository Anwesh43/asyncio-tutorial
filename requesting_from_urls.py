import asyncio
import aiohttp
async def fetch_resp(n=1):
     async with aiohttp.ClientSession() as session:
         async with session.get('http://localhost:8000/task/{0}'.format(n)) as resp:
                print(await resp.text())
                print("fetch task from server with {0} seconds".format(n))

async def dummy_task():
    print("completed dummy task")

ioloop = asyncio.get_event_loop()
tasks = [fetch_resp(2),fetch_resp(3),dummy_task()]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()

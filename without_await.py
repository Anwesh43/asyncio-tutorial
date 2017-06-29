import asyncio
import time
@asyncio.coroutine
def task(n):
    time.sleep(n)
    print("completed after {0} seconds".format(n))


ioloop = asyncio.get_event_loop()
tasks = [task(4),task(3),task(2)]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()

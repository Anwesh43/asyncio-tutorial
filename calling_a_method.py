import asyncio
import time
loop = asyncio.get_event_loop()
def print_hello():
    time.sleep(2)
    print("hello")

def print_hi(loop):
    time.sleep(2)
    print("hi")
    loop.stop()
loop.call_soon(print_hello)
loop.call_soon(print_hi,loop)
loop.run_forever()
loop.close()

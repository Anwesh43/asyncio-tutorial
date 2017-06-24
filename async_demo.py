import asyncio
async def task1():
    await asyncio.sleep(2)
    print("inside task1")

async def task2():
    await asyncio.sleep(3)
    print("inside task2")

async def task3():
     await asyncio.sleep(1)
     print("inside task3")

ioloop = asyncio.get_event_loop()
wait_task = asyncio.wait([ioloop.create_task(task1()),ioloop.create_task(task2()),ioloop.create_task(task3())])
ioloop.run_until_complete(wait_task)
ioloop.close()

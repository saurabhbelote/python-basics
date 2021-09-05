import asyncio

async def task1 ():
    print("send first Email")
    asyncio.create_task(task2())
    await asyncio.sleep(2)
    print('First email reply')

async def task2():
    print('send second email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('First email reply')


async def task3():
    print('send second email')
    await asyncio.sleep(2)
    print('First email reply')

asyncio.run(task3())
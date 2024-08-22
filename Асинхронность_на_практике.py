import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        await asyncio.sleep(power / 5)
        print(f'Силач {name} поднял {ball} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Паша', 10))
    task2 = asyncio.create_task(start_strongman('Вася', 15))
    task3 = asyncio.create_task(start_strongman('Коля', 20))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())

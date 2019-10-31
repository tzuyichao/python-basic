import asyncio

async def example():
    print('Staring example coroutin.')
    await asyncio.sleep(1)
    print("Finish example coroutin.")

asyncio.run(example())
print('main')
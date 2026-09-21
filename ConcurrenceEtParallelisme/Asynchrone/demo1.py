import asyncio
import time

async def worker(caractere):
    for i in range(0, 10):
        await asyncio.sleep(1)
        print(caractere, flush=True, end="")
    print(caractere + " end " )

async def main():
    print("main begin")
    t1 = asyncio.create_task(worker("*"))
    t2 = asyncio.create_task(worker("$"))
    await t1 
    await t2
    print("main end")

print("MT begin")
asyncio.run(main())
print("MT end")
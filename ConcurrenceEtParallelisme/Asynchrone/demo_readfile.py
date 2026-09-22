import asyncio, time, aiofiles, os

print(__file__) #c:\Users\PaulE\perfectionnement\ConcurrenceEtParallelisme\Asynchrone\demo_readfile.py
print(os.path.dirname(__file__)) #c:\Users\PaulE\perfectionnement\ConcurrenceEtParallelisme\Asynchrone

async def read_file(file_name):
    async with aiofiles.open(file_name) as file:
        result = await file.read()
        print(f"{result}")

async def main():
    t1 = asyncio.create_task(read_file(os.path.dirname(__file__)+"/file1.txt"))
    t2 = asyncio.create_task(read_file(os.path.dirname(__file__)+"/file2.txt"))
    t3 = asyncio.create_task(read_file(os.path.dirname(__file__)+"/file3.txt"))
    await t1
    await t2
    await t3

asyncio.run(main())

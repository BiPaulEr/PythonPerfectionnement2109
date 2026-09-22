import asyncio, time

async def read_file(file_name):
    time.sleep(3)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

async def main():
    t1 = asyncio.create_task(read_file("file1"))
    t2 = asyncio.create_task(read_file("file2"))
    t3 = asyncio.create_task(read_file("file3"))
    await t1
    await t2
    await t3

asyncio.run(main())

import asyncio, time, random

async def do_work(duration):
    await asyncio.sleep(duration)
    return f"Finished work in {duration} seconds"

async def main():
    durations = [ 3, 1, 4, 2]
    taches = [do_work(duration) for duration in durations]
    for task in asyncio.as_completed(taches):
        result = await task
        print(f"resultat -> {result}")

asyncio.run(main())

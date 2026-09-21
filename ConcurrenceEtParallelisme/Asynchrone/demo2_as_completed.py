import asyncio
import time
import random

async def capteur(caractere):
    resultat = random.randint(0, 10)
    await asyncio.sleep(resultat)
    print(caractere," ",  str( resultat))
    return resultat

async def main():
    print("main begin")
    tasks = [capteur("1"), capteur("2"), capteur("3")]
    for task in asyncio.as_completed(tasks):
        res = await task
        print(res)
    print("main end")

print("MT begin")
asyncio.run(main())
print("MT end")
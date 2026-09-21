import asyncio
import time
import random

async def capteur(caractere):
    await asyncio.sleep(2)
    resultat = random.randint(0, 100)
    print(caractere," ",  str( resultat))
    return resultat

async def main():
    print("main begin")
    resultats = await asyncio.gather(capteur("1"), capteur("2"), capteur("3"))
    print(resultats)
    print(" moyenne ", str(sum(resultats) / 3))
    print("main end")

print("MT begin")
asyncio.run(main())
print("MT end")
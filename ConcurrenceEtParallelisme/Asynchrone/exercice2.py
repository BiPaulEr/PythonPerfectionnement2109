import asyncio, time, random

async def fetch_weather(city):
    await asyncio.sleep(3)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}

async def main():
    villes = [ "City1", "City2", "City3"]
    taches = [fetch_weather(name_ville) for name_ville in villes]
    resultats = await asyncio.gather(*taches) #[{'ville': 'City1', 'température': 18}, {'ville': 'City2', 'température': 23}, {'ville': 'City3', 'température': 19}]
    moyenne = sum([temperature['température'] for temperature in resultats]) / len(villes)
    print(f"moyenne : {moyenne}")

asyncio.run(main())

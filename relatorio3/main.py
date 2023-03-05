from database import Database
from save_json import writeAJson


db = Database(database="dex", collection="pokemons")
db.reset_database()

pokemons = db.collection.find()
#for pokemon in pokemons: #printando ela
#    print(pokemon)

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

pokemon = db.collection.find({"id": { "$lte": 151 }})
writeAJson(pokemon, "first_generation")

pokemon = db.collection.find({"id": { "$gte": 387, "$lte": 493}})
writeAJson(pokemon, "fourth_generation")

pokemon = db.collection.find({"id": { "$gte": 722 }})
writeAJson(pokemon, "seventh_generation")

pokemon = db.collection.find({"type": "Water", "base.Speed": { "$gte": 30 }})
writeAJson(pokemon, "pokemon_water")

pokemon = db.collection.find({"type": "Water", "base.Speed": { "$gte": 30 }})
writeAJson(pokemon, "pokemon_water")

pokemon = db.collection.find({"name.english": { "$regex": "^B" }})
writeAJson(pokemon, "pokemon_letter_b")





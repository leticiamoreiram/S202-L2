from Database import Database
class ZoologicoDAO:
    def __init__(self):
        self.db = Database(database='zoologico', collection='animais')
        self.collection = self.db.collection

    def create(self, animal):
        habitats = []

        for habitat in animal.habitats:
            habitats = {
                "nomeHabitat": habitat.nomeHabitat,
                "tipoAmbiente": habitat.tipoAmbiente,
                "Cuidador": {
                    "nomeCuidador": habitat.cuidadorAmbiente.nomeCuidador,
                    "documento": habitat.cuidadorAmbiente.documento
                }
            }
            habitats.append(habitats)
        self.collection.insert_one({
            "nomeAnimal": animal.nomeAnimal,
            "especie": animal.especie,
            "idade": animal.idade,
            "habitat": habitats
        })
        print(f"Animal {animal.nomeAnimal} criado com sucesso.")

    def read(self, verAnimal: str):
        print(f"Animal {verAnimal} buscado com sucesso.")
        return self.collection.find({"nomeAnimal": verAnimal})

    def update(self, animalAlterado: str, novoNome: str):
        print(f"Animal {animalAlterado} atualizado com o nome {novoNome}.")
        return self.collection.update_one(
            {"nomeAnimal": animalAlterado},
            {
                "$set": {"nomeAnimal": novoNome}
            }
        )

    def delete(self, animalDeletado: str):
        print(f"Animal {animalDeletado} deletado.")
        return self.collection.delete_one({"Nome do Animal": animalDeletado})


from Database import Database


class ZoologicoDAO:
    def __init__(self):
        self.db = Database(database='zoologico', collection='animais')
        self.collection = self.db.collection

    def create(self, animal):
        habitats = []

        for habitat in animal.habitats:
            habitats = {
                "Nome do habitat": habitat.nomeHabitat,
                "Tipo de Ambiente": habitat.tipoAmbiente,
                "Cuidador": {
                    "Nome do Cuidador": habitat.cuidadorAmbiente.nomeCuidador,
                    "Documento do Cuidador": habitat.cuidadorAmbiente.documento
                }
            }
            habitats.append(habitats)

        self.collection.insert_one({
            "Nome do Animal": animal.nomeAnimal,
            "Especie": animal.especie,
            "Idade": animal.idade,
            "Habitat": habitats
        })
        print(f"Animal {animal.nomeAnimal} criado com sucesso.")


    def read(self, verAnimal: str):
        print(f"Animal {verAnimal} buscado com sucesso.")
        return self.collection.find({"Nome do Animal": verAnimal})

    def update(self, animalAlterado: str, novoNome: str):
        print(f"Animal {animalAlterado} atualizado com o nome {novoNome}.")
        return self.collection.update_one(
            {"Nome do Animal": animalAlterado},
            {
                "$set": {"Nome do Animal": novoNome}
            }
        )

    def delete(self, animalDeletado: str):
        print(f"Animal {animalDeletado} deletado.")
        return self.collection.delete_one({"Nome do Animal": animalDeletado})


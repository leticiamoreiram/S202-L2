from typing import List

from ZoologicoDAO import ZoologicoDAO
from Database import Database
from Cuidador import Cuidador
from Habitat import Habitat
from Animal import Animal

if __name__ == '__main__':

    zoo = ZoologicoDAO()

    while True:
        print("-------- Zoologico --------")
        print("Escolha uma opção:")
        print("1. Cadastro")
        print("2. Verificar")
        print("3. Atualizar Dados")
        print("4. Deletar Dados")
        print("5. Sair")

        opcao = int(input())

        if opcao == 1:

            print("****** Cadastro do Cuidador ******")
            nomeCuidador = input("Nome do cuidador: ")
            documento = input("Documento do cuidador: ")
            cuidador = Cuidador(nomeCuidador, documento)

            print("****** Cadastro de Habitats ******")
            habitats = []
            print("Quantos habitats deseja cadastrar para este cuidador? ")
            qtd = int(input())

            for i in range(qtd):
                nomeHabitat = input("Nome do Habitat: ")
                tipoAmbiente = input("Tipo de Ambiente: ")
                cuidadorAmbiente = cuidador

                habitats.append(Habitat(nomeHabitat, tipoAmbiente, cuidador))

            print("****** Cadastro de Animal ******")
            nomeAnimal = input("Nome do animal: ")
            especie = input("Especie: ")
            idade = int(input("Idade: "))
            animal = Animal(nomeAnimal, especie, idade, habitats)

            zoo.create(animal)

        if opcao == 2:

            print("****** Verificar ******")
            verAnimal = input("Insira o nome do animal que deseja verificar: ")
            zoo.read(verAnimal)

        if opcao == 3:

            animalAlterado = input("Insira o nome do animal que deseja alterar: ")
            novoNome = input("Insira novo nome do animal: ")
            zoo.update(animalAlterado, novoNome)

        if opcao == 4:
            animalDeletado = input("Insira o nome do animal que deseja deletar")
            zoo.delete(animalDeletado)

        if opcao == 5:
            break
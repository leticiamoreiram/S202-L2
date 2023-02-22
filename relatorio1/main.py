class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.nome + " esta emitindo um som: " + self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
        print(self.nome + " mudou a cor para " + self.cor)

# animal1 = Animal("simba", 1, "gato", "cinza", "miau")
# print(animal1.nome)
# print(animal1.idade)
# print(animal1.especie)
# print(animal1.cor)
# print(animal1.som)
# print("")
# print(animal1.emitir_som())
# print(animal1.mudar_cor("amarelo"))

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.nome + " esta emitindo um som: " + self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        print(self.nome + " é de tamanho " + self.tamanho)


nome = input("Digite o nome do elefante: ")
idade = input("Digite a idade do elefante: ")
especie = input("Digite a especie do elefante: ")
cor = input("Digite a cor do elefante: ")
som = "KJEFBIAERGI"
tamanho = input("Digite o tamanho do elefante: ")

elefante = Elefante(nome, idade, especie, cor, som, tamanho)


if especie == "africano" and int(idade) < 10:
    elefante.mudar_tamanho("pequeno")
    #print(elefante.tamanho)
    elefante.som = "Paaah"
    #print(elefante.som)
    elefante.trombar()
elif especie == "africano" and int(idade) >= 10:
    elefante.mudar_tamanho("grande")
    elefante.som = "PAHHHHHH"
    elefante.trombar()
else:
    print(elefante.nome + " possui tamanho " + elefante.tamanho)
    elefante.trombar()

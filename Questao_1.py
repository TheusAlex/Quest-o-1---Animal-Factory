from typing import List

class Animal:
    def fazer_som(self):
        pass

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

class Cachorro(Animal):
    def fazer_som(self):
        return "Auau"

class AnimalFactory:
    _instance = None
    historico: List[str] = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnimalFactory, cls).__new__(cls)
        return cls._instance

    def criar_animal(self, tipo):
        if tipo == "1":
            animal = Gato()
        elif tipo == "2":
            animal = Cachorro()
        else:
            raise ValueError("Tipo de animal inválido")

        som = animal.fazer_som()
        self.historico.append(f"{tipo} {som}")
        return som

def main():
    factory = AnimalFactory()

    print("*********************************")
    print("           Bem vindo             ")
    print("*********************************")

    while True:
        entrada = input("Digite '1' para GATO, '2' para CACHORRO, 'histórico' para ver o histórico, ou '3' para encerrar: ")

        if entrada.lower() == "histórico":
            for item in factory.historico:
                print(item)
        elif entrada == "3":
            print("Encerrando a execução.")
            break
        else:
            try:
                som = factory.criar_animal(entrada)
                print(f"Output: {som}")
            except ValueError as e:
                print(f"Erro: {e}")

if __name__ == "__main__":
    main()

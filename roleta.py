import random


class Roleta:
    def __init__(self, linked_list):
        self.roleta_list = linked_list
        self.items_initial = ["A", "B", "C"]
        self.diff = 3

        self.initialize()

    def initialize(self):
        for item in self.items_initial:
            self.roleta_list.enqueue(item)

    def update(self, item):
        ## Implementei esse logica, pois se eu adicionar um item igual a diff nao aumenta e sim diminui
        if item in self.roleta_list.getItemsList():
            print(f"O item '{item}' já existe na roleta. Por favor, escolha um item diferente.")
            return
        
        self.roleta_list.enqueue(item)
        self.diff += 1
        print(f"Novo item '{item}' adicionado à roleta. Dificuldade aumentada!")

    def play(self): 
        result = self.roleta_list.spin(random.randint(self.diff * 2, self.diff * 8))

        print("\n\nCarregando resultado...")

        return result
    
    def print_items_roleta(self):
        print("\n" + "-" * 30 + "\nELEMENTOS DA ROLETA" + "\n")
        self.roleta_list.printList()
        print("-" * 30)
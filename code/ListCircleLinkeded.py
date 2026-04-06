# A base (nó) da lista
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A lista
class CircleLinkedList:
    def __init__(self):
        self.tail = None # Na lista linkada guardamos o ultimo

    def enqueue(self, data):
        node = Node(data)

        # Se for o primeiro no
        if self.tail is None:
            self.tail = node # O ultimo é ele mesmo
            self.tail.next = self.tail # Aponta para si
        else:
            node.next = self.tail.next # O no (tail) aponta para o primeiro
            self.tail.next = node # O antigo tail aponta para o novo no
            self.tail = node # Defini o ultimo no (tail)

    def dequeue(self):
        if not self.tail:
            print("Empty List")
            return None

        firstItem = self.tail.next

        if firstItem is self.tail:
            self.tail = None
            return firstItem.data

        self.tail.next = firstItem.next # O segundo agora é o primeiro
        return firstItem.data

    def printList(self):
        if self.tail is None:
            print("Empty List.")
            return

        element = [] # Tipo um cache
        nodeActual = self.tail.next # Peguei o primeiro

        while True:
            element.append(nodeActual.data)
            nodeActual = nodeActual.next

            if nodeActual is self.tail.next:
                break

        print(element)

myList = CircleLinkedList()

myList.enqueue("A")
myList.enqueue("B")
myList.enqueue("C")

myList.printList()

item = myList.dequeue()
print(f"Item Removido: {item}")

myList.printList()
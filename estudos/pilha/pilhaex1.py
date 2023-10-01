from node import Node


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def push(self, elem):
        # insere um elemento na pilha
        pass
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1


    def pop(self):
        # remove o elemento do topo da pilha 
        if self.size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empyty")
    
    def peek(self):
        # retorna o topo da pilha sem remover
        if self.size > 0:
            return self.top.data
        raise IndexError("The stack is empty")


 
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size
    

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    


#    def append(self,elem):
#        if self.head:
#           # insercao quando a lista ja possui elementos
#           pointer = self.head
#            while(pointer.next):
#                pointer = pointer.nex
#            pointer.next = Node(elem)
#        else:
#            # primeira insercao
#            self.head = Node(elem)
#        self._size = self._size + 1
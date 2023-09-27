from node import Node


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def push(self, elem):
        # insere um elemento na pilha
        pass
    
    def pop(self):
        # remove o elemento do topo da pilha 
    
    def peek(self):
        # retorna o topo da pilha sem remover

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
 
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size
import io
class SingleLinkedList:
    class Node:
        def __init__ (self, value):
            self.value = value
            self.linked_next_node = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #convertir la info del archivo en nodos
    def convertirNodos(self):
        with io.open("Archivo.txt",'r',encoding = 'utf-8') as data_file:
            for line in data_file.readlines():
                self.add_node_tail(line)
            data_file.close()

    #mostrar nodos
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        #Recoremos la lista hasta que no existan nodos
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.linked_next_node
        print(f"{node_list} La cantidad de nodos {self.length}")

    #añade nodo al inicio de la lista
    def add_node_head (self, value):
        new_node = self.Node(value)
        if self.head == None and self.tail==None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.linked_next_node = self.head
            self.head = new_node
        self.length+=1
    
    def add_node_tail (self, value):
        new_node = self.Node(value)
        if self.head == None and self.tail==None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.linked_next_node = new_node
            self.tail = new_node
        self.length+=1
        
    #insertar en una posicion deseada
    def insert(self, index, value):
        if index == self.length + 1:
            return self.add_node_tail(value)
        elif index == 1:
            return self.add_node_head(value)
        elif not (index >= self.length+1 or index <= 0):
            new_node = self.Node(value+'\n')
            previous_node = self.get(index-1)
            nodos_siguientes = previous_node.linked_next_node
            previous_node.linked_next_node = new_node
            new_node.linked_next_node = nodos_siguientes
            self.length += 1
        else:
            return None
    #get
    def get(self, index):
        if index == self.length:
            return self.tail
        elif index == 1:
            return self.head
        elif not (index >= self.length + 1 or index <= 0):
            current_node = self.head
            contador = 1
            while contador != index:
                current_node = current_node.linked_next_node
                contador  += 1
            return current_node
        else:
            return None

    #actualizar informacion del archivo desde los nodos
    def update(self,archivo):
        current_node = self.head
        self.clear_file()
        with io.open(archivo,'w',encoding='utf-8') as data_file:
            while(current_node != None):
                data_file.write(current_node.value+'\n')
                current_node = current_node.linked_next_node
        data_file.close()
    #actualizar el valor de un nodo
    def update_nodo(self,index, value):
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            nodo_objetivo.value = value
        else:
            return 0

    #eliminar en una posicion
    def remove(self, index):
        if index == 1:
            self.delete_first_node()
        elif index == self.length:
            self.delete_final_node()
        elif not (index >= self.length+1 or index <= 0):
            nodos_anteriores = self.get(index - 1)
            nodo_removido = nodos_anteriores.linked_next_node
            nodos_anteriores.linked_next_node = nodo_removido.linked_next_node
            nodo_removido.linked_next_node = None
            self.length -= 1
            print(f'El valor del nodo removido es: {nodo_removido.value}')
        else:
            return None

    #eliminar al final
    def delete_final_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            new_tail = current_node
            while(current_node.linked_next_node != None):
                new_tail = current_node
                current_node = current_node.linked_next_node
            self.tail = new_tail
            self.tail.linked_next_node = None
            self.length -= 1
            print(f'El valor del nodo eliminado es {current_node.value}') 

    #eliminar al inicio
    def delete_first_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.head
            self.head = remove_node.linked_next_node
            remove_node. linked_next_node = None
            self.length -= 1
            print(f'El valor del nodo eliminado es {remove_node.value}') 
    #reverse list
    def reverse_list (self):
        reverse_nodes = None
        current_node = self.head
        self.tail = current_node
        while (current_node != None):
            linked_next_node = current_node.linked_next_node
            current_node.linked_next_node = reverse_nodes
            reverse_nodes = current_node
            current_node = linked_next_node
        self.head = reverse_nodes
        return self.head

    #limpiar archivo
    def clear_file(self):
        archivo = open('Archivo.txt','w')
        archivo.write('')
        archivo.close()

    #limpiar nodos
    def clear_nodes(self):
        self.head = None
        self.tail = None
        self.length = 0


import io
from singleLinkedList import SingleLinkedList
inst_singleLinkedList = SingleLinkedList()

class MenuNodos:
    def getmenu(self):
        inst_singleLinkedList.convertirNodos()
        inst_singleLinkedList.show_nodes_list()
        while True:
            try:    
                print("\n     <<Qué desea continuar haciendo>>\n")
                opcion = input(" a - Insertar un nuevo nodo\n b - Eliminar un nodo\n c - Consultar por el valor de un nodo especificado\n d - Editar el valor de un nodo existente en la lista\n e - Invertir el contenido de la lista\n f - Vaciar la lista\n g - Salir del sistema \n>> ")
                while opcion != 'a' and opcion != 'b' and opcion != 'c' and opcion != 'd' and opcion != 'e' and opcion != 'f' and opcion != 'g':
                    print("\nDato invalido,por favor intentelo nuevamente\n")
                    opcion = input(" a - Insertar un nuevo nodo\n b - Eliminar un nodo\n c - Consultar por el valor de un nodo especificado\n d - Editar el valor de un nodo existente en la lista\n e - Invertir el contenido de la lista\n f - Vaciar la lista\n g - Salir del sistema \n>> ")
                if opcion == 'a':
                    print("Desea insertarlo:\n")
                    while True:
                        try:
                            opcionInsert = int(input("1 - Al inicio\n2 - Al final\n3 - En una posicion especifica\n>> "))
                            if opcionInsert != 1 and opcionInsert != 2 and opcionInsert != 3:
                                print("Numero invalido, intentelo nuevamente\n")
                            elif opcionInsert == 1:
                                value = input("Ingrese el valor del nuevo nodo: ")
                                inst_singleLinkedList.add_node_head(value)
                                inst_singleLinkedList.show_nodes_list()
                                inst_singleLinkedList.update('Archivo.txt')
                                print("Contenido añadido correctamente")
                                break 
                            elif opcionInsert == 2:
                                value = input("Ingrese el valor del nuevo nodo: ")
                                inst_singleLinkedList.add_node_tail(value)
                                inst_singleLinkedList.show_nodes_list()
                                inst_singleLinkedList.update('Archivo.txt')
                                print("Contenido añadido correctamente")
                                break
                            elif opcionInsert == 3:
                                value = input("Ingrese el valor del nuevo nodo: ")
                                index = int(input("\nIngrese la posicion deseada: "))
                                inst_singleLinkedList.insert(index,value)
                                inst_singleLinkedList.show_nodes_list()
                                inst_singleLinkedList.update('Archivo.txt')
                                print("Contenido añadido correctamente")
                                break
                        except ValueError:
                            print("Valor invalido, intentelo nuevamente\n")
                elif opcion == 'b':
                    print("Desea eliminarlo:\n")
                    while True:
                        try:
                            opcionInsert = int(input("1 - Al inicio\n2 - Al final\n3 - En una posicion especifica\n>> "))
                            if opcionInsert != 1 and opcionInsert != 2 and opcionInsert != 3:
                                print("Numero invalido, intentelo nuevamente\n")
                            elif opcionInsert == 1:
                                inst_singleLinkedList.delete_first_node()
                                inst_singleLinkedList.update('Archivo.txt')
                                print("Contenido eliminado correctamente")
                                break 
                            elif opcionInsert == 2:
                                inst_singleLinkedList.delete_final_node()
                                inst_singleLinkedList.update('Archivo.txt')
                                print("Contenido eliminado correctamente")
                                break
                            elif opcionInsert == 3:
                                index = int(input("\nIngrese la posicion deseada: "))
                                inst_singleLinkedList.remove(index)
                                inst_singleLinkedList.update('Archivo.txt')
                                print("Contenido eliminado correctamente")
                                break
                        except ValueError:
                            print("Valor invalido, intentelo nuevamente\n")
                elif opcion == 'c':
                    while True:
                        try:
                            index = int(input("Ingrese el numero del nodo que desea consular: "))
                            if inst_singleLinkedList.get(index) != None:
                                print(f'\nEl valor del nodo solicitado es: {inst_singleLinkedList.get(index).value}')
                            else:
                                print("El nodo soliciado no existe")
                            break
                        except ValueError:
                            print("Dato invalido, por favor intentelo nuevamente")
                elif opcion == 'd':
                    while True:
                        try:
                            index = int(input("\nIngrese el numero del nodo que desea editar: "))
                            value = input("\nIngese el nuevo valor del nodo: ")
                            if inst_singleLinkedList.update_nodo(index,value) == 0:   
                                print("El nodo solicitado no existe")
                            else:
                                inst_singleLinkedList.update_nodo(index,value)
                                inst_singleLinkedList.update('Archivo.txt')
                                print("El valor del nodo ha sido actualizado")
                                break
                        except ValueError:
                            print("Dato invalido, porfavor intentelo nuevamente")
                elif opcion == 'e':
                    inst_singleLinkedList.reverse_list()
                    inst_singleLinkedList.show_nodes_list()
                    inst_singleLinkedList.update('Archivo.txt')
                elif opcion == 'f':
                    inst_singleLinkedList.clear_nodes()
                    inst_singleLinkedList.update('Archivo.txt')
                    print("Vaciado completado\n")
                elif opcion == 'g':
                    print("\n       <<Fue un placer, hasta la proxima>>")
                    break
            except ValueError:
                print("Error")
from operaciones import Operaciones
inst_operaciones = Operaciones()
class MenuInicial:
    def getmenu(self):
        while True:
            try:
                opcion = int(input("\nIngrese la opcion deseada\n>> 1 - Leer el archivo\n>> 2 - Editar el archivo\n>> 3 - Sobreescribir el archivo\n>> 4 - Cancelar\n>> "))
                if opcion != 1 and opcion != 2 and opcion != 3 and opcion !=4:
                    print("Numero invalido, por favor intentelo nuevamente\n")
                    #Leer el archivo como lista
                elif opcion == 1:
                    print("\n     <<La infomracion que contiene el archivo es>>\n")
                    inst_operaciones.LeerArchivo()
                    print("\n")
                    #Editar el archivo
                elif opcion == 2:
                    inst_operaciones.EditarArchivo()

                    #Sobreescribir el archivo
                elif opcion == 3:
                    inst_operaciones.SobreescribirArchivo()

                    #Cancelar
                elif opcion == 4:
                    break
            except ValueError:
                print("Dato invalido, por favor intentelo nuevamente\n")
import io
class Operaciones:
    def __init__(self):
        self.file = open("Archivo.txt",'r')
    #Leer archivo
    def LeerArchivo(self):
        with io.open("Archivo.txt",'r',encoding = 'utf-8') as data_file:
            for line in data_file.readlines():
                print(line,end='')
            data_file.close()
    #Editar la informacion del archivo
    def EditarArchivo(self):
        info = input("\n>>Ingrese la informacion que desea añadir al archivo:\n")
        with io.open("Archivo.txt",'a',encoding = 'utf-8') as data_file:
            data_file.write('\n'+info)
        data_file.close()
    
    def SobreescribirArchivo(self):
        text = input('\n>>Ingrese el nuevo contenido del archivo:\n')
        with io.open('Archivo.txt','w', encoding='utf-8') as data_file:
            data_file.write(text)
        data_file.close()



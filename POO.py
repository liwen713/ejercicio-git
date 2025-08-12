#class Persona: #para nombres de clases se usa PascalCase
#    def __init__(self, nombre, apellido, edad): #método. init tiene que ver con crear.
#        self.nombre=nombre
#        self.apellido=apellido
#        self.edad=edad
#    
#    def saludar(self):
#        print(f"Hola! Mi nombre es {self.nombre}") #no print en clases

#ana=Persona("Ana", "Lopez", 18)
#juan=Persona("Juan", "Rosales", 19)

class Vehiculo:
    def __init__(self, marca, modelo, patente, kilometraje):
        self.marca=marca
        self.modelo=modelo
        self.patente=patente
        self.kilometraje=kilometraje
    
    def mostrar_datos(self):
        return(f"Marca del vehículo ingresado: {self.marca}. \nModelo del vehículo ingresado: {self.modelo}. \nPatente del vehiculo: {self.patente}. \nKilometraje del vehiculo ingresado: {self.kilometraje}")

marca=input("Ingrese la marca del vehículo: ")
modelo=input("Ingrese la modelo del vehículo: ")
patente=input("Ingrese la patente del vehículo: ")
kilometraje=int(input("Ingrese el kilometraje del vehículo: "))

vehiculos=Vehiculo(marca, modelo, patente, kilometraje)

print("--------------------")

print(vehiculos.mostrar_datos())

# metodo __nombre__
# metodo __str__ : es llamado por defecto si no se le pasa ningun parametro 
# metodo __len__ : 

#self.nombre : dato publico.
#self._nombre : protegido. solo acceden las clases que son hijas.
#self.__ : privadas. no se puede acceder al dato.
#a que le doy acceso (lectura escritura)
#buena practica definir todos en privado. 
# atributos deben ser privados.
#Juan.set_nombre("José")

class Persona:
    def __init__ (self, nombre, apellido, estado=""):
        self.__nombre=nombre
        self.__apellido=apellido
    
    def set_nombre(self):
         return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def __str__ (self):
        return f"Id: {self.__id}, Nombre: {self.__nombre}"

from POO import persona #importar una clase
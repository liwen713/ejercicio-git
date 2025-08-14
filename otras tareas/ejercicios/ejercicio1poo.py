class Cuenta:
    def __init__ (self, titular, nro_cuenta, monto=""):
        self.__titular=titular
        self.__nro_cuenta=nro_cuenta
        self.__monto=monto

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular=titular
    
    def get_nro_cuenta(self):
        return self.__nro_cuenta
    
    def get_monto(self, monto):
        return self.__monto

    def mostrar(self):
        return f"Titular de la cuenta: {self.__titular}. \nNúmero de cuenta: {self.__nro_cuenta}. \nMonto de la cuenta: {self.__monto}."
    
    def ingresar(self, cantidad):
        cantidad=input(int("Escriba la cantidad de dinero a ingresar."))
        get_monto()= #dormir
        if cantidad < 0:
            print("No se puede ingresar una cantidad menor a 0.")
            return
           
    def retirar(self,antidad):
        return f"Cantidad retirada"
        
mi_cuenta=Cuenta
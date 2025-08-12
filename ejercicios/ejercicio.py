class Cuenta:
    def __init__ (self, titular, nroCuenta, monto): #init es el constructor
        self.__titular=titular
        self.__nroCuenta=nroCuenta
        self.__monto=monto 
    
    def get_titular(self):
        return self.__titular
    
    def get_nroCuena(self):
        return self.__nroCuenta
    
    def set_monto(self, monto):
        self.__monto=monto
    
    def __str__(self):
        return 
num1=int(input("Ingrese el primer número"))
num2=int(input("Ingrese el segundo número"))
num3=int(input("Ingrese el tercer número"))
numMenor=0

if num1>num2 and num3>num2:
    numMenor=num2
elif num2>num1 and num3>num1: 
    numMenor=num1
else:
    numMenor=num3

print("El número menor es " + str(numMenor))
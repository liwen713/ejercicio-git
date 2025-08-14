inventario={"sillas": 10,
"mesas": 4}

def agregar_producto(producto, stock):
    inventario[producto]=stock

def mostrar_inventario():
    return inventario

while True:
    opcion_menu=input("Ingrese A-Agregar, M-Mostrar, S-Salir")
    if opcion_menu=="A":
        producto=input("Ingrese el nombre del producto a agregar")
        stock=input("Ingrese el stock que hay del producto")
        agregar_producto(producto, stock)
        print(inventario)
    elif opcion_menu=="M":
        print(mostrar_inventario())
    elif opcion_menu=="S":
        break
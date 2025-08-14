guerreros = [
    {'Nombre': 'Sebastián', 'Habilidad': 'Arquero', 'Lealtad': 8, 'Cambio_Lealtad': 'S'},
    {'Nombre': 'Sergio', 'Habilidad': 'Lanzador', 'Lealtad': 9, 'Cambio_Lealtad': 'N'},
    {'Nombre': 'Ivana', 'Habilidad': 'Combatiente', 'Lealtad': 10, 'Cambio_Lealtad': 'S'}
]

def opciones():
    while True:
        print("==== ¡Gestiona tu ejército fantástico! ====")
        print("Opciones:")
        print("C. Crear un guerrero")
        print("M. Mostrar los guerreros disponibles")
        print("H. Mostrar los guerreros por habilidad")
        print("L. Mostrar los guerreros que cambiaron de lealtad")
        print("S. Salir")
        opcion = input("¿Qué deseas hacer?: ").upper()

        if opcion == "C":
            registro_guerreros()
        elif opcion == "M":
            mostrar_guerreros()
        elif opcion == "H":
            mostrar_por_habilidad()
        elif opcion == "L":
            filtrar_por_cambio_lealtad()
        elif opcion == "S":
            break
        else: 
            print ("Esta no es una opción válida.")
        print("---------------------------")

def registro_guerreros():
    while True:
        print("==== Creador de guerreros ====")
        nombre=input("Ingrese el nombre del guerrero a crear: ")
        if nombre==" ":    
            break

        habilidad=input("Ingresa, en una palabra, la habilidad de combate que tendrá tu guerrero: ")
        nivel_lealtad=int(input("Del 1 al 10, ¿qué tan leal te es tu personaje?: "))
        cambio_lealtad=input("¿Tu guerrero ha cambiado su lealtad recientemente? (S/N): ")

        guerreros.append(
            {'Nombre': nombre,
            'Habilidad': habilidad, 
            'Lealtad': nivel_lealtad,
            'Cambio_Lealtad': cambio_lealtad
            })

        salida=input("¿Deseas crear otro personaje? (S/N) ")
        if salida=="N":
            break
        else:
            print(f"Personaje agregado: {nombre}. Habilidad: {habilidad}. Lealtad: {nivel_lealtad}.")
        print("----------------------------")

def mostrar_guerreros():
    print("==== Lista de guerreros ====")
    for i, guerrero in enumerate(guerreros, 1):
        print(f"Guerrero #{i}")
        print(f"Nombre: {guerrero['Nombre']}")
        print(f"Habilidad: {guerrero['Habilidad']}")
        print(f"Nivel de Lealtad: {guerrero['Lealtad']}/10")
        print(f"Cambio de Lealtad: {'Sí' if guerrero['Cambio_Lealtad'] == 'S' else 'No'}")
        print("---------------------------")

def mostrar_por_habilidad():
    print("==== Mostrar guerreros por habilidad ====")
    guerreros_ordenados_por_habilidad = sorted(guerreros, key=lambda g: g['Habilidad'])
    
    for i in range(len(guerreros_ordenados_por_habilidad)):
        guerrero = guerreros_ordenados_por_habilidad[i]
        print(f"Índice: {i+1}, Nombre: {guerrero['Nombre']}")
        print(f"Habilidad: {guerrero['Habilidad']}")
        print("----------------------------")

def filtrar_por_cambio_lealtad():
    lealtad_cambiada = []

    for guerrero in guerreros:
        if guerrero['Cambio_Lealtad'] == 'S':
            lealtad_cambiada.append(guerrero['Nombre'])
    
    print("==== Guerreros que cambiaron su lealtad ====")
    for i in range(len(lealtad_cambiada)):
        print(f"{i+1}. {lealtad_cambiada[i]}")
    print("----------------------------")

opciones() #zvhju2v
from object import Reproductor

def menu():
    generos_iniciales = ['Rock', 'Pop', 'Jazz', 'Blues', 'Classical'] #para pasar como parámetros requeridos, porque main llamaba a reproductor sin parámetros pero el constructor tenía 3 parámetros obligatorios.
    artistas_iniciales = ['Queen', 'John Lennon', 'Eagles', 'The Beatles']
    canciones_iniciales = []

    reproductor = Reproductor(
        generos=generos_iniciales,
        artistas=artistas_iniciales, 
        canciones=canciones_iniciales
    )

    while True:
        print("="*50)
        print("===== Bienvenido a tu reproductor de música =====")
        print("="*50)
        print("===== ¿Qué deseas hacer? =====")
        print("A. Agregar una canción")
        print("R. Reproducir una canción")
        print("B. Buscar artistas, álbumes, géneros o canciones")
        print("V. Ver tus canciones guardadas")
        print("S. Salir")
        opcion = input("Ingresa la opción deseada: ").upper()

        if opcion == "A":
            reproductor.agregar_cancion()

        elif opcion== "R":
            reproductor.reproducir_cancion()

        elif opcion=="B":
            reproductor.buscar()

        elif opcion=="V":
            reproductor.ver_canciones()

        elif opcion=="S":
            break

        else: 
            print("="*50)
            print("¡Opción no válida! Por favor, elige una opción válida.")
            print("="*50)
            input("Presiona 'Enter' para continuar...")
    

menu()

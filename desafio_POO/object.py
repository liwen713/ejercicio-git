class Reproductor:

    def __init__ (self, generos, artistas, canciones, guardados=""):
        self.__generos=generos
        self.__artistas=artistas
        self.__canciones=canciones
        self.__guardados=guardados

        self.__lista=[
            {'Canción': 'Bohemian Rhapsody', 'Artista': 'Queen', 'Genero': 'Rock'},
            {'Canción': 'Con Mi Guitarra', 'Artista': 'SUPERUVA', 'Genero': 'Punk'},
            {'Canción': 'Bye Bye', 'Artista': 'Vilma Palma e Vampiros', 'Genero': 'Rock'}
        ]
    
    def __len__(self):
        return len(self.__lista)
    
    def agregar_cancion(self):
        print("==== Agrega una canción nueva ====")
        nombre=input("Ingresa el nombre de la canción que quieras agregar: ")
        artista=input("Ingresa el nombre del artista: ")
        genero=input("Ingresa el genero musical al que tu canción pertenece: ")
        nueva = {'Canción': nombre, 'Artista': artista, 'Genero': genero}
        self.__lista.append(nueva)
        print("="*50)
        print(f"Canción '{nombre}' de '{artista}' agregada exitosamente.")
        print("="*50)
        input("Presiona 'Enter' para continuar...")

    def reproducir_cancion(self):
        print("==== Reproduce una canción ====")
        nombre=input("Ingresa el nombre de la canción a reproducir: ")
        encontrada=False

        while True:
            for cancion in self.__lista:
                if cancion['Canción'].lower() == nombre.lower():
                    print("="*50)
                    print(f"Reproduciendo: {cancion['Canción']} - {cancion['Artista']}")
                    print("="*50)
                    break
                encontrada=True
            input("Presiona 'Enter' para continuar...")
            return

        if not encontrada: 
            print("Canción no encontrada.")
            input("Presiona 'Enter' para continuar...")

    def buscar(self):
        print("==== Buscador ====")
        print("1. Buscar por canción")
        print("2. Buscar por artista")
        print("3. Buscar por género")

        opcion=input("Elige una de las opciones: ")

        if opcion == "1":
            self._buscar_por_cancion()
        elif opcion == "2":
            self._buscar_por_artista()
        elif opcion == "3":
            self._buscar_por_genero()
        else:
            print("Opción no válida.")

    def _buscar_por_cancion(self):
        nombre=input("Ingresa el nombre de la canción a buscar: ")
        encontrada=False

        for cancion in self.__lista:
            if nombre.lower() in cancion['Canción'].lower():
                print("="*50)
                print(f"{cancion['Canción']} - {cancion['Artista']} ({cancion['Genero']})")
                print("="*50)
                encontrada=True

        if not encontrada:
            print("="*50)
            print("No se encontraron canciones.")
            print("="*50)

        input("Presiona 'Enter' para continuar...")
    
    def _buscar_por_artista(self):
        artista=input("Ingresa el nombre del artista a buscar: ")
        encontrada=False
        
        for cancion in self.__lista:
            if artista.lower() in cancion['Artista'].lower():
                print("="*50)
                print(f"{cancion['Canción']} - {cancion['Artista']} ({cancion['Genero']})")
                print("="*50)
                encontrada=True

        if not encontrada:
            print("="*50)
            print("No se encontraron canciones de ese artista.")
            print("="*50)
        
        input("Presiona 'Enter' para continuar...")
            
    def _buscar_por_genero(self):
        genero=input("Ingresa el género a buscar: ")
        encontrada=False
        
        for cancion in self.__lista:
            if genero.lower() in cancion['Genero'].lower():
                print("="*50)
                print(f"{cancion['Canción']} - {cancion['Artista']} ({cancion['Genero']})")
                encontrada=True

        if not encontrada:
            print("="*50)
            print("No se encontraron canciones de ese genero.")
            print("="*50)
        
        input("Presiona 'Enter' para continuar...")
    
    def ver_canciones(self):
        print("==== Tus canciones guardadas ====")

        if not self.__lista:
            print("="*50)
            print("No tienes canciones guardadas.")
            print("="*50)
            return

        print(f"Tienes {len(self.__lista)} canciones:")
        for i, cancion in enumerate(self.__lista, 1):
            print(f"{i}. {cancion['Canción']} - {cancion['Artista']} ({cancion['Genero']})")
        
        input("Presiona 'Enter' para continuar...")
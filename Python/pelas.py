# Base de datos con más de 10 películas (cada una es un vector de palabras)
peliculas = {
    "Matrix": ["ciencia", "ficcion", "accion", "computadora"],
    "Shrek": ["comedia", "animacion", "ogro", "burro"],
    "Titanic": ["romance", "drama", "barco", "hielo"],
    "Terminator": ["ciencia", "ficcion", "accion", "robot"],
    "Toy Story": ["comedia", "animacion", "juguetes", "vaquero"],
    "El Padrino": ["drama", "mafia", "crimen", "familia"],
    "Inception": ["ciencia", "ficcion", "accion", "mente"],
    "Nemo": ["comedia", "animacion", "pez", "oceano"],
    "Gladiador": ["accion", "drama", "roma", "pelea"],
    "Avatar": ["ciencia", "ficcion", "accion", "alien"],
    "Coco": ["comedia", "animacion", "musica", "familia"],
    "John Wick": ["accion", "venganza", "disparos", "perro"]
}

# --- 1. ENCONTRAR SIMILITUD DE DOS PELÍCULAS ---
print("Pelas disponibles:", ", ".join(peliculas.keys()))
peli1 = input("Ingresa la primera película: ")
peli2 = input("Ingresa la segunda película: ")

# Sacamos los vectores de las películas (si no existe, bota lista vacía)
vector_peli1 = peliculas.get(peli1, [])
vector_peli2 = peliculas.get(peli2, [])

# Calcular la cantidad de palabras compartidas (igualito a tu ejemplo del spam)
similitud = sum([1 for word in vector_peli1 if word in vector_peli2])

if similitud >= 2:
    print("¡Alerta! Estas películas son recontra parecidas.")
elif similitud == 1:
    print("Tienen un aire, pero no son tan iguales.")
else:
    print("Nada que ver, son totalmente distintas.")

# --- 2. BUSCAR PELÍCULAS POR PALABRA CLAVE ---
busqueda = input("\nIngresa una palabra clave para buscar (ej. accion, comedia): ").lower()

# Buscar en qué vectores aparece la palabra clave
encontradas = [peli for peli, vector in peliculas.items() if busqueda in vector]

if encontradas:
    print(f"Pelas que tienen '{busqueda}': {encontradas}")
else:
    print("Este diccionario no tiene pelas con esa palabra.")
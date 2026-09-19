# Orden de los géneros del vector:
# [romance, drama, catastrofe, ciencia_ficcion, aventura, accion,
# historica, animacion, comedia, thriller, fantasia, misterio]

peliculas = {
    "titanic": [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "avatar": [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    "gladiator": [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    "shrek": [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    "matrix": [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    "forrest gump": [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "toy story": [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    "el señor de los anillos": [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    "el rey leon": [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    "memento": [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    "interestelar": [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
}


# Géneros de cada película

palabras_clave = {
    "titanic": ["romance", "drama", "catastrofe"],
    "avatar": ["ciencia ficcion", "aventura", "accion"],
    "gladiator": ["accion", "drama", "historica"],
    "shrek": ["animacion", "comedia", "aventura"],
    "matrix": ["ciencia ficcion", "accion", "thriller"],
    "forrest gump": ["drama", "comedia", "romance"],
    "toy story": ["animacion", "comedia", "aventura"],
    "el señor de los anillos": ["fantasia", "aventura", "accion"],
    "el rey leon": ["animacion", "drama", "aventura"],
    "memento": ["thriller", "misterio", "drama"],
    "interestelar": ["ciencia ficcion", "drama", "aventura"]
}


# COMPARAR DOS PELÍCULAS

pelicula1 = input("Ingresa la primera película: ").lower()
pelicula2 = input("Ingresa la segunda película: ").lower()


# Comprobar si existen o están bien escritas

if pelicula1 not in peliculas or pelicula2 not in peliculas:

    print("Una de las películas no existe o está mal escrita.")

else:

    vector_pelicula1 = peliculas[pelicula1]
    vector_pelicula2 = peliculas[pelicula2]

    similitud = sum(
        [a * b for a, b in zip(vector_pelicula1, vector_pelicula2)]
    )

    print("La similitud es:", similitud)


# BUSCAR PELÍCULA POR GÉNERO

busca_peli = input("Escribe un género o palabra clave: ").lower()

encontrada = False

for pelicula, generos in palabras_clave.items():

    if busca_peli in generos:

        print("Película encontrada:", pelicula)

        encontrada = True


# Si el género no existe o está mal escrito

if encontrada == False:

    print("El género no existe o está mal escrito.")

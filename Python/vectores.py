#Vector de la pelícla Matrix
matrix = [1, 0, 1, 0, 1] # [Acción, Comedia, Ciencia Ficción, Drama, Suspenso]
#Vector de la película El Padrino
el_padrino = [0, 0, 0, 1, 0] # [Acción, Comedia, Ciencia Ficción, Drama, Suspenso]
#Calcular la similitud entre las películas.
similitud = sum([a * b for a, b in zip (matrix, el_padrino)])
print(f"La similitud entre Matrix y El Padrino es: {similitud}")

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

# lista = []


def velocidades(velocidad):
    promedio_velocidad:float = sum(velocidad)/len(velocidad)
    
    lista_mayores = [posicion for posicion,elemento in enumerate(velocidad) if elemento > promedio_velocidad]
    
    # Opté por dejar la comprension porque tres lineas de codigo para una sola lista es suficiente
    
    # for posicion,elemento in enumerate(velocidad):
    #     if elemento > promedio_velocidad:
    #         lista.append(posicion)
        
    return lista_mayores

posiciones=velocidades(velocidad)
print(posiciones)
# print(lista)
from sys import argv

umbral:int = int(argv[1])
lista:list = []

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}




def diccionario_filtrado(diccionario,umbral,argumento='mayor'):
    if argumento == 'mayor':
        filtrado = {k:v for k,v in diccionario.items() if v >= umbral}
    elif argumento == 'menor':
        filtrado = {k:v for k,v in diccionario.items() if v <= umbral}
    else:
        return "Lo sentimos, no es una operación valida"
        
    lista.append(filtrado.keys())
    return filtrado
    
if len(argv) == 2:

    filtro = diccionario_filtrado(precios,umbral)
    lista_filtrada = list(lista[0])
    print("Los productos mayores al umbral son: " + ', '.join(lista_filtrada))
else:
    argumento:str = argv[2].lower()
    
    if argumento == 'otro':
        filtro = diccionario_filtrado(precios,umbral,argumento)
        print(filtro)
    else:
        filtro = diccionario_filtrado(precios,umbral,argumento)
        lista_filtrada = list(lista[0])
        print("Los productos mayores al umbral son: " + ', '.join(lista_filtrada))
        

    

    



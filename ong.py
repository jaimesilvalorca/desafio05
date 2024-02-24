def factorial(numero):
    lista_factorial = [posicion for posicion in range(1, numero + 1)]
    resultado = 1
    for num in lista_factorial:
        resultado *= num
    return resultado

def productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def calcular(**kwargs):
    resultados = []
    for key, value in kwargs.items():
        if 'fact' in key:
            resultados.append(factorial(value))
            print(f"El factorial de {value} es: {factorial(value)}")
        elif 'prod' in key:
            resultados.append(productoria(value))
            print(f"La productoria {value} es: {productoria(value)}")
    return resultados

resultados = calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)



def maior_impar(lista):
    # Retorna o maior número impar presente
    # numeros_impares = []
    # for numero in lista:
    #     if numero % 2 != 0:
    #         numeros_impares.append(numero)
    # return max(numeros_impares)

    return max(list(filter(lambda numero: numero % 2 != 0, lista)))


# Encontra o menor número ímpar presente
def menor_impar(lista):
    return min(list(filter(lambda numero: numero % 2 != 0, lista)))


# Encontra o menor e maior número ímpar presente
def menor_maior_impar(lista):
    impar_maior = max(list(filter(lambda numero: numero % 2 != 0, lista)))
    impar_menor = min(list(filter(lambda numero: numero % 2 != 0, lista)))
    print(
        f'O maior número ímpar é:\t{impar_maior}\nO menor número ímpar é:\t{impar_menor}')

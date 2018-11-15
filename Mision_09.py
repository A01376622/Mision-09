#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que usa listas


#Función que recibe una lista y regresa otra lista con los números pares de la primera lista
def extraerPares(listaEnteros):
    listaPares = []

    for k in listaEnteros:

        if k % 2 == 0:
            listaPares.append(k)

    return listaPares


#Función que recibe una lista y regresa otra lista con los valores que son mayores a un elemento previo.
def extraerMayoresPrevio(lista):
    listaMayores = []

    if len(lista) > 0:

        datoInicial = lista[0]

        for k in lista:

            if k > datoInicial:
                listaMayores.append(k)

            datoInicial = k

    return listaMayores


#Función que regresa una nueva lista con parejas de datos intercambiadas.
def intercambiarParejas(lista):
    listaIntercambiada = []
    valores = len(lista)

    if valores % 2 == 0:
        for k in range(0,len(lista),2):
            listaIntercambiada.append(lista[k+1])
            listaIntercambiada.append(lista[k])

    else:
        for k in range(1,len(lista),2):
            listaIntercambiada.append(lista[k])
            listaIntercambiada.append(lista[k-1])

        listaIntercambiada.append(lista[len(lista)-1])

    return listaIntercambiada


#Función que recibe una lista e intercambia el valor mayor y el menor de la lista
def intercambiarMM(lista):
    if len(lista)>1:
        valorMayor = lista[0]
        valorMenor = lista[0]
        indexMayor = 0
        indexMenor = 0

        for k in range(0,len(lista)):

            if lista[k] > valorMayor:
                valorMayor = lista[k]
                indexMayor = k

            if lista[k] < valorMenor:
                valorMenor = lista[k]
                indexMenor = k

        lista.remove(valorMenor)
        lista.remove(valorMayor)
        lista.insert(indexMenor, valorMayor)
        lista.insert(indexMayor, valorMenor)

    return lista


#Función que recibe una lista y calcula el promedio de los valores, quitando el valor mayor y el menor.
def promediarCentro(lista):
    listaPromedio = lista[:]

    if len(listaPromedio) > 2:
        valorMenor = listaPromedio[0]
        valorMayor = listaPromedio[0]

        for k in range(0, len(listaPromedio)):
            if listaPromedio[k] < valorMenor:
                valorMenor = listaPromedio[k]

            if listaPromedio[k] > valorMayor:
                valorMayor = listaPromedio[k]

        listaPromedio.remove(valorMayor)
        listaPromedio.remove(valorMenor)
        numeroValores = len(listaPromedio)

        promedio = sum(listaPromedio)//numeroValores

    else:
        promedio = 0

    return promedio


#Función que recibe una lista y regresa una dupla con la media y la desviación estándar.
def calcularEstadistica(lista):
    n = len(lista)

    if n > 1:
        mean = sum(lista)/n
        suma = 0

        for xi in lista:
            dif = (xi-mean)**2
            suma += dif

        deviation = (suma/(n-1)) ** 0.5

        info = (mean, deviation)
    elif n > 0 and n < 1:
        mean = sum(lista)/n
        info = (int(mean),0)

    else:
        info = (0,0)

    return info


#Función que recibe una lista, elimina los valores 13 y los números alrededor de ellos, y regresa la suma de los valores.
def calcularSuma(lista):

    if lista.count(13):
        while lista.count(13) > 0:
            if lista.index(13) == 0:
                if len(lista)>1:
                    lista.remove(lista[0])
                    lista.remove(lista[0])
                else:
                    lista.remove(lista[0])

            elif lista.index(13) == len(lista) - 1:
                lista.pop()
                lista.pop()

            else:
                index13 = lista.index(13)
                lista.remove(lista[index13 - 1])
                lista.remove(lista[index13 - 1])
                lista.remove(lista[index13 - 1])

    suma = sum(lista)

    return suma


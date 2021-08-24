miLista = [34, 93, 19, 58, 12, 28, 95, 37, 23, 80, 57, 82,
           55, 48, 21, 39, 53, 65, 30, 32, 84, 64, 44, 68, 36]


def quickSort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        # print(izquierda+["-"]+centro+["-"]+derecha)
        return quickSort(izquierda)+centro+quickSort(derecha)
    else:
        return lista


print(miLista)
print(quickSort(miLista))

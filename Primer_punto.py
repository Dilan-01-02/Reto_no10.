'''
Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

'''
def llenadoDeLista(x) -> list:
    """Función que realiza el llenado de la lista de tamaño x recibido como parámetro

    Args:
        x (int): Primer parámetro.
            Tamaño del arreglo

    Returns:
        list: lista
    """
    lista = []
    for i in range(x):
        # Ciclo for en el que se ingresan los números a la lista
        n = float(input("Ingrese el elemento "+str(i+1)+" de la lista: "))
        lista.append(n)
    return lista

def promedioDeLista(x:int,lista:list) -> float:
    """Función que calcula el promedio de los números ingresados a una lista recibida como parámetro de tamaño x también recibido como parámetro

    Args:
        x (int): Primer parámetro.
            Tamaño de la lista
        lista: Segundo parámetro.
            Lista a la cual se le calculará el promedio de los números ingresados en ella 

    Returns:
        float: promedio
    """
    promedio : float = 0 
    for i in lista:
        # Ciclo for que calcula el promedio de los números ingresados a la lista
        promedio = promedio + i
    promedio /= x
    return promedio 

if __name__ == "__main__":
    x = int(input("Ingrese la longitud de la lista: "))
    # Llamado de la función llenadoDeLista y envío del parámetro x
    lista = llenadoDeLista(x)
    # Llamado de la función promedioDeLista y envío de los parámetros x y lista
    promedioLista = promedioDeLista(x,lista)
    print('El promedio de los números ingresados en la lista "'+str(lista)+'" es: '+str(promedioLista))
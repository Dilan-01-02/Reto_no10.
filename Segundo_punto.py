'''
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

'''
def llenadoDeArreglo(x:int,a:int) -> list:
    """Función que realiza el llenado de los arreglos de tamaño x recibido como parámetro

    Args:
        x (int): Primer parámetro.
            Tamaño del arreglo
        a (int): Segundo parámetro.
            Número del arreglo

    Returns:
        list: lista
    """
    arreglo = []
    print("=====================")
    print("LLENADO DEL ARREGLO "+str(a))
    for i in range (x):
        # Bucle for que realiza el llenado de los arreglos 
        n = float(input("Ingrese el elemento "+str(i+1)+" del arreglo: "))
        arreglo.append(n)
    return arreglo

def calculoDelProductoPunto(x:int,arreglo1:list,arreglo2:list) -> float:
    """Función que calcula el producto punto de dos listas recibidas como parámetros ambas de tamaño x

    Args:
        x (int): Primer parámetro.
            Tamaño de ambos arreglos
        arreglo1 (list): Segundo parámetro.
            Primer arreglo
        arreglo2 (list): Segundo parámetro.
            Segundo arreglo

    Returns:
        list: punto
    """
    punto : float = 0
    for i in range(x):
        # Bucle for que realiza el cálculo del producto punto entre ambas listas
        punto = punto + arreglo1[i]*arreglo2[i]
    return punto

if __name__ == "__main__":
    x = int(input("Ingrese el tamaño de las 2 listas: "))
    # Llamado de la función llenadoDeArreglo y envío de los parámetros x y 1
    arreglo1 = llenadoDeArreglo(x,1)
    # Llamado de la función llenadoDeArreglo y envío de los parámetros x y 2
    arreglo2 = llenadoDeArreglo(x,2)
    # Llamado de la función calculoDelProductoPunto y envío de los parámetros x, arreglo1 y arreglo2
    productoPunto = calculoDelProductoPunto(x,arreglo1,arreglo2)
    print(str(arreglo1)+" · "+str(arreglo2)+" = "+str(productoPunto))

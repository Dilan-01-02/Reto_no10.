'''
Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

'''
# Importación de la función llenadoDeLista del archivo "Primer_punto"
from Primer_punto import llenadoDeLista

def acomodacionDeCeros(arreglo:list) -> list:
    """Función que acomoda los ceros presentes en un arreglo recibido como parámetro al final del mismo

    Args:
        arreglo (list): Primer parámetro.
            Arreglo al cual se le acomodarán los ceros presentes en el, al final del mismo 

    Returns:
        list: arreglo
    """
    for i in arreglo:
        # Bucle for que acomoda los ceros presentes en un arreglo al final del mismo
        if i == 0:
            arreglo.append(i)
            arreglo.remove(0)
    return arreglo

if __name__ == "__main__":
    x = int(input("Ingrese la longitud de la lista: "))
    # Llamado de la función llenadoDeLista y envío del parámetro x
    arreglo = llenadoDeLista(x)
    # Llamado de la función acomodacionDeCeros y envío del parámetro arreglo  
    arregloCeros = acomodacionDeCeros(arreglo)
    print("El arreglo con los ceros al final es: "+str(arregloCeros))
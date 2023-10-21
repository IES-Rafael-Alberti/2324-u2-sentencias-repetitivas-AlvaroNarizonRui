"""
Ejercicio 1:
Escribir un programa que pida al usuario una palabra y 
la muestre por pantalla 10 veces.
"""
def mostrarPalabra(palabra, veces):
    salida = ""
    while veces > 0:
        salida += palabra + "\n"
        veces -= 1
    return salida
if __name__ == "__main__":
    #Entrada
    palabra = input("Escribe una palabra: ")
    veces = 10
    #Procesamiento
    salida = mostrarPalabra(palabra, veces)
    #Salida
    print(salida)

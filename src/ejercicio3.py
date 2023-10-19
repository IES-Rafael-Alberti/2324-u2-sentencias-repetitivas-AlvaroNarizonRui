"""
Ejercicio 3¶
Escribir un programa que pida al usuario un número entero positivo y muestre
 por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def numerosImpares(numero):
    impares = ""
    for i in range(1,numero+1,1):
        if i % 2 != 0:
            impares += str(i) + ","
    return impares

if __name__ == "__main__":
    #Entrada
    numero = int(input("Escribe un numero : "))
    #Procesamiento
    impares = numerosImpares(numero)
    #Salida
    print(f"Los numeros impares hasta el {numero} son : {impares}")
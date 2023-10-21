# Ejercicio 6¶
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
# de altura el número introducido.

# *
# **
# ***
# ****
# *****
def creadorTriangulo(numero):
    contenedor = ""
    if numero > 0:
        for i in range(1,numero+1,1):
            contenedor += str(i*"*" + "\n")
        return contenedor
    else:
        contenedor = "Error"
        return contenedor


if __name__ == "__main__":
    #Entrada
    numero = int(input("Escribe un número entero positivo"))
    #Procesamiento
    triangulo = creadorTriangulo(numero)
    if triangulo == "Error":
        print("Error: Introdujiste un número que no es positivo entero")
    else:
        #Salida
        print(f"El número que introdujiste: {numero} \n Resultado: {triangulo}")
        

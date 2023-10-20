#Ejercicio 4¶
#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def cuentaAtras(numero):
    contador = ""
    if numero <= 0:
        contador = "Error"
        return "Error"
    else:
        for i in range(numero,-1,-1):
            if str(i) == "0":
                contador += str(i)
            else:
                contador += str(i) + ","
        return contador



if __name__ == "__main__":
   #Entrada
    numero = int(input("Escribe un número entero positivo : "))
    #Procesamiento
    contador = cuentaAtras(numero)
    #Salida
    if contador == "Error":
        print(f"No se puede introducir un número que sea menor o igual a 0")
    else:
        print(f"El número que introdujiste: {numero} \n Su cuenta atrás: {contador}")
    
# Ejercicio 7¶
# Escribir un programa que muestre por pantalla 
# la tabla de multiplicar del 1 al 10.

def tablaMultiplicar():
    tablaMultiplicar = ""
    for i in range(10):
        for j in range(11):
            tablaMultiplicar += str(i) + " x " + str(j) + " = " + str(i*j) + "\n"
    return tablaMultiplicar

if __name__ == "__main__":
    #Procesamiento
    tablaMultiplicar = tablaMultiplicar()
    #Salida
    print(tablaMultiplicar)
"""
Ejercicio 2¶
Escribir un programa que pregunte al usuario su edad y muestre
por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def añosVividos(edad):
    cumpleaños = ""
    for i in range(1,edad+1,1):
        cumpleaños += str(i) + ","
    return cumpleaños


if __name__ == "__main__":
    #Entrada
    edad = int(input("Escribe tu edad : "))
    #Procesamiento
    cumpleaños = añosVividos(edad)
    #Salida
    print(f"Los años que viviste hasta los {edad} son: {cumpleaños}")
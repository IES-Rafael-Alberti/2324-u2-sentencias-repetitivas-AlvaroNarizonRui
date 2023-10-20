#Ejercicio 5¶
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año 
# que dura la inversión.

# Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 

def calculadoraInteres(años,interes_anual,cantidad):
    interes_completo = ""
    for i in range(1,años+1,1):
        cantidad *= i + interes_anual/100
        cantidad = int(cantidad)
        interes_completo += str(cantidad) + ","
        lista_interes = interes_completo.split(",")
        print(lista_interes)
    return lista_interes

if __name__ == "__main__":
    #Entrada
    cantidad = int(input("Escribe una cantidad a invertir: "))
    interes_anual = int(input("Escribe el porcentaje de interes_anual: "))
    años = int(input("Escribe el número de años : "))
    #Procesamiento
    calculadora = calculadoraInteres(años,interes_anual,cantidad)
    #Salida
    contador = 0
    for i in range(1,años+1,1):
        print(f"En el año {i} : {calculadora[contador]} euros")
        contador+=1

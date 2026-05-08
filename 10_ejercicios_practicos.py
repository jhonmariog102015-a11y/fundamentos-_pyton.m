#ejercicio 1
nombre="pepito"
producto=20000
promedio=8.5

print("mi nombre es",nombre,"y comprare un que vale",producto,"y tengo un ",promedio)

#ejercico 2
# Programa que lee tipos de datos y realiza operaciones

# Lectura de datos
entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
numero_float = float(input("Ingrese un número float: "))

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

# Suma de los tres números
suma = entero1 + entero2 + numero_float
print("\nLa suma de los tres números es:", suma)

# Mostrar el entero mayor
if entero1 > entero2:
    print("El entero mayor es:", entero1)
elif entero2 > entero1:
    print("El entero mayor es:", entero2)
else:
    print("Los dos enteros son iguales")

# División del float con el resto de la división de los enteros
resto = entero1 % entero2

if resto != 0:
    resultado = numero_float / resto
    print("Resultado de la división:", resultado)
else:
    print("No se puede dividir entre 0 porque el resto es 0")

# Concatenación de cadenas
concatenacion = cadena1 + " " + cadena2
print("Concatenación de cadenas:", concatenacion)



#ejercicio 3

base=5
exponente=3
resultado=base**exponente
print(F"EL resultado de {base} elevado a la {exponente} es: {resultado}")


#ejercicio 4

import math


numeros = [2, 8, 9, 27, 28, 55, 121]


for numero in numeros:
    raiz = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz}")

#ejercico 5
}
nombre = input("Ingrese el nombre del estudiante: ")


nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))


promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5


print("\nNombre del estudiante:", nombre)
print("Promedio final:", promedio)

#ejercicio 6

# Crear variables
numeroUno = 8
numeroDos = 2

# Mostrar valores originales
print("Valores originales:")
print("numeroUno =", numeroUno)
print("numeroDos =", numeroDos)

# Intercambiar valores usando una variable auxiliar
auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar

# Mostrar resultados
print("\nValores intercambiados:")
print("numeroUno =", numeroUno)
print("numeroDos =", numeroDos)

#ejercicio 7

# Crear variable booleana
Estado = (5 == 2) or (2 > 1)

# Mostrar resultado
print("El valor de Estado es:", Estado)

#ejercicio 8

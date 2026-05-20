#tuplas
tupla = (1, 2, 3, 4, 5)
print(type(tupla))

tupla2="a", "b", "c"
print(type(tupla2))

tupla3=("hola",)
print(type(tupla3))

tupla4= tuple("hola")
print(tupla4)

tupla_mixta = (1, "hola", 3.14, [1, 2, 3], (4, 5))
print(tupla_mixta)

tupla_aprendises = ("Jhon", "Maria", "Carlos", "Ana")
print(tupla_aprendises[0]) 
#tupla_aprendises[0] = "Pedro"  # Esto generará un error porque las tuplas son inmutables

print(tupla_aprendises[1:3])
print(tupla_aprendises[-1])
print(tupla_aprendises[-2:])
tupla_suma = tupla + tupla2
print(tupla_suma)
tupla_repetida = tupla * 2


tupla_aprendises.count("Maria")
tupla_aprendises.index("Carlos")
print(len(tupla))

print(tupla_aprendises)
aprendises_lista = list(tupla_aprendises)
print(aprendises_lista)
aprendises_lista.append("Pedro")
print(aprendises_lista)
tupla_aprendises = tuple(aprendises_lista)
print(tupla_aprendises)

print("Jhon" in tupla_aprendises)#true
print("Luis" in tupla_aprendises)#false

#empaquetado y desempaquetado de tuplas
programa1 ="adso"
programa2 = "desarrollo de software"
programa3 = "analisis y diseño de sistemas"

# Desempaquetado
tupla_programas = (programa1, programa2, programa3)
print(tupla_programas)

tupla_desempaquetada = ("adso", "desarrollo de software", "analisis y diseño de sistemas")
programa1, programa2, programa3 = tupla_desempaquetada
print(programa1)
print(programa2)
print(programa3)

#tupla de ciudades
ciudades = ("Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena")

ciudad_1, ciudad_2, ciudad_3, ciudad_4, ciudad_5 = ciudades
print(ciudad_1)
print(ciudad_2)
print(ciudad_3)
print(ciudad_4)
print(ciudad_5)

for ciudad in ciudades:
    print(ciudad)
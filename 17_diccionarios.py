# ============================================================
#   ARCHIVO 17: Fundamentos de Diccionarios
# ============================================================
# Este archivo explica el uso de estructuras clave-valor.
# Cubre: creación de diccionarios, acceso a datos, métodos 
# de actualización (update), eliminación (pop) y el manejo
# de diccionarios anidados para estructuras complejas.
# ============================================================
#son estructuras de datos que almacenan pares de clave-valor
#se pueden crear con llaves {} o con la función dict()
#ejemplo de diccionario
persona = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

diccionario_vacio = {}

#diccionario aprendiz
aprendiz = {
    "nombre": "Jhon",
    "edad": 30,
    "apellido": "Mendez",
    "ficha": 123456,
    "programa": "Fundamentos de la programación"
}
print(type(aprendiz))#class 'dict'
print(aprendiz)

#obtener un valor de un diccionario
print(aprendiz["nombre"]) #Jhon
print(aprendiz["edad"]) #30
print(aprendiz["apellido"]) #Mendez
print(aprendiz["ficha"]) #123456
print(aprendiz["programa"]) #Fundamentos de la programación
#obtener la clave de un diccionario
print(aprendiz.keys()) #dict_keys(['nombre', 'edad', 'apellido', 'ficha', 'programa'])
#obtener los valores de un diccionario
print(aprendiz.values()) #dict_values(['Jhon', 30, 'Mendez', 123456, 'Fundamentos de la programación'])
#obtener los pares clave-valor de un diccionario
print(aprendiz.items())

#agregar un nuevo elemento al diccionario
aprendiz["programa"] = "cocina"
print(aprendiz)


#metodo update() para actualizar un diccionario 
aprendiz.update({"programa": "cocina"})
aprendiz.update({"edad": 31})
print(aprendiz)

#comprobar pertenencia (in) en un diccionario
if "nombre" in aprendiz:
    print("esta es una clave del diccionario")

#recorrer un diccionario con un bucle for
for clave in aprendiz.keys():   
    print(clave) #imprime las claves del diccionario    

#recorrer solo los valores del diccionario
for valor in aprendiz.values():
    print(valor) #imprime los valores del diccionario

#recorrer las claves y valores del diccionario
for clave, valor in aprendiz.items():
    print(f"{clave}: {valor}") #imprime las claves y valores del diccionario

#eliminar un elemento del diccionario con pop()
aprendiz.popitem() #elimina el ultimo elemento del diccionario
print(aprendiz)

aprendiz.pop("programa") #elimina el elemento con la clave "programa"
print(aprendiz)

aprendiz.clear() #elimina todos los elementos del diccionario
print(aprendiz) #imprime un diccionario vacio {}

#diccionarios anidados
persona = {
    "Aprendiz_1": {
        "nombre": "Jhon",
        "edad": 30,
        "direccion": {
            "calle": "Calle 123",
            "ciudad": "Bogotá"
        }
    },
    "Aprendiz_2": {
        "nombre": "Maria",  
        "edad": 25,
        "direccion": {
            "calle": "Calle 456",
            "ciudad": "Medellín"
        }   
},"aprendiz_3": {
        "nombre": "Carlos",
        "edad": 28,
        "direccion": {
            "calle": "Calle 789",
            "ciudad": "Cali"
        }
    }
}
#acceder a un valor de un diccionario anidado
print(persona["Aprendiz_1"]["nombre"]) #Jhon

#recorrer un diccionario anidado
for aprendiz_id, info in persona.items():
    print(f"{aprendiz_id}:")
    for clave, valor in info.items():
        print(f"  {clave}: {valor}")

# Nota: La sección de conjuntos se maneja en el archivo 20_actividad4_set.py
print("\nSección de diccionarios finalizada con éxito.")

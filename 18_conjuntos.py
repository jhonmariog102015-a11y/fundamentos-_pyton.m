#conjuntos
#estructura de conjunto
conjunto = set()
print(type(conjunto)) #imprime el conjunto

#creaccion de un nuevo conjunto
lenguajes = {"Python", "Java","Python","C++", "JavaScript","Java"}
print(lenguajes) #imprime el conjunto de lenguajes

#metodo de modificar un conjunto
frutas = {"manzana", "banana", "naranja"}
frutas.add("pera") #agrega un nuevo elemento al conjunto
frutas.remove("banana") #elimina un elemento del conjunto
frutas.discard("uva") #elimina un elemento del conjunto sin generar error si no existe
elemento_eliminado = frutas.pop() #elimina un elemento aleatorio del conjunto y lo devuelve
print(frutas) #imprime el conjunto de frutas
print(elemento_eliminado) #imprime el elemento eliminado

#verificar pertenencia:0(1)
print("manzana" in frutas) #True
print("banana" in frutas) #False

#union de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union_conjuntos = conjunto1.union(conjunto2) #union de conjuntos
print(union_conjuntos) #imprime la union de los conjuntos

#interseccion de conjuntos
interseccion= {"manzana", "banana", "naranja"}
conjunto3 = {"manzana", "pera", "naranja"}
interseccion_conjuntos = interseccion.intersection(conjunto3) #interseccion de conjuntos
print(interseccion_conjuntos) #imprime la interseccion de los conjuntos

#diferencia de conjuntos
diferencia_conjuntos = conjunto1.difference(conjunto2) #diferencia de conjuntos
print(diferencia_conjuntos) #imprime la diferencia de los conjuntos
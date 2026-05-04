nombre = "john doe"
edad= 30
altura = True
correo="jhonmariog10201@gmail.com"
telefono=123456789
cedula=1234567890

cedula_=str(cedula)
edad_=float(edad)
altura_=bool(altura)
telefono_=int(telefono)

print (type(nombre),nombre)
print (type(edad),edad)
print (type(telefono),telefono)
print (type(altura),altura)
print (type(correo),correo)

telefono_init=int(telefono) 
print (type(telefono_init),telefono_init)

edad_init=float(edad)
print (type(edad_init),edad_init)

#sdkd
if True:
    print("hola")
    for i in range(5):
        print("hola")

#jdd
valor_1=float(input("ingrese un valor: "))
valor_2=float(input("ingrese otro valor: "))

tipo_operacion=input("ingrese la operacion a realizar:" \
"\n1. suma\n2. resta\n3. multiplicacion\n4. division\n")

if tipo_operacion=="1":
    resultado=valor_1+valor_2
    print("el resultado de la suma es: ",resultado)
elif tipo_operacion=="2":
    resultado=valor_1-valor_2
    print("el resultado de la resta es: ",resultado)
elif tipo_operacion=="3":
    resultado=valor_1*valor_2
    print("el resultado de la multiplicacion es: ",resultado)   
elif tipo_operacion=="4":
    if valor_2!=0:
        resultado=valor_1/valor_2
        print("el resultado de la division es: ",resultado)
       
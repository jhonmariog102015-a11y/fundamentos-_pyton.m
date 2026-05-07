# ============================================================
#   EJERCICIO 1: Tipos de datos y conversión de tipos (casting)
# ============================================================
# En este ejercicio se declaran variables de distintos tipos
# de datos básicos en Python: str, int, float, bool.
# Luego se imprime cada variable junto con su tipo usando type().
# Por último, se practica el casting: convertir un tipo en otro.
# ============================================================
# --- Declaración de variables con distintos tipos de datos ---
nombre = "jhon mario"  # str   → texto
edad = 20  # int   → número entero
altura = 1.75  # float → número decimal
activo = True  # bool  → verdadero / falso
correo = "jhonmariog10201@gmail.com"  # str   → texto
telefono = 123456789  # int   → número entero
cedula = 1234567890  # int   → número entero

# --- Mostrar el tipo y el valor de cada variable ---
print("=" * 45)
print("   TIPOS DE DATOS ORIGINALES")
print("=" * 45)
print(f"  nombre → {type(nombre).__name__:6}  : {nombre}")
print(f"  edad   → {type(edad).__name__:6}  : {edad}")
print(f"  altura → {type(altura).__name__:6} : {altura}")
print(f"  activo → {type(activo).__name__:6}  : {activo}")
print(f"  correo → {type(correo).__name__:6}  : {correo}")
print(f"  telefono → {type(telefono).__name__:6}  : {telefono}")
print(f"  cedula → {type(cedula).__name__:6}  : {cedula}")

# --- Casting: convertir variables de un tipo a otro ---
# str()   convierte a texto
# float() convierte a decimal
# int()   convierte a entero
# bool()  convierte a booleano
print("\n" + "=" * 45)
print("   CONVERSIÓN DE TIPOS (CASTING)")
print("=" * 45)

cedula_str = str(cedula)  # int  → str
edad_float = float(edad)  # int  → float
telefono_int = int(telefono)  # int  → int (sin cambio, solo demostración)

print(f"cedula como str → {type(cedula_str).__name__:6}  : '{cedula_str}'")
print(f"edad   como float → {type(edad_float).__name__:6} : {edad_float}")
print(f"telef. como int → {type(telefono_int).__name__:6}  : {telefono_int}")

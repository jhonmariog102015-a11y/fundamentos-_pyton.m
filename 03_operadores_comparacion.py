# ============================================================
#   EJERCICIO 3: Operadores de comparación
# ============================================================
# Los operadores de comparación comparan dos valores y
# siempre devuelven un booleano: True o False.
#
#   ==   igualdad           !=  diferente (distinto)
#   <    menor que          >   mayor que
#   <=   menor o igual que  >=  mayor o igual que
#
# Se muestran ejemplos que resultan True y luego False,
# para entender exactamente cuándo cada operador se cumple.
# ============================================================

print("=" * 45)
print("   OPERADORES DE COMPARACIÓN")
print("=" * 45)

# --- Ejemplos que dan True ---
print("\n  ── Resultados True ──")
print(f"  1 == 1  → {1 == 1}   (son iguales)")
print(f"  2 != 1  → {2 != 1}   (son distintos)")
print(f"  1 < 2   → {1 < 2}   (1 es menor que 2)")
print(f"  2 > 1   → {2 > 1}   (2 es mayor que 1)")
print(f"  1 <= 1  → {1 <= 1}   (1 es menor o igual a 1)")
print(f"  1 >= 1  → {1 >= 1}   (1 es mayor o igual a 1)")

# --- Ejemplos que dan False ---
print("\n  ── Resultados False ──")
print(f"  2 == 1  → {2 == 1}  (2 y 1 no son iguales)")
print(f"  1 != 1  → {1 != 1}  (1 y 1 sí son iguales, no son distintos)")
print(f"  1 < 1   → {1 < 1}  (1 no es estrictamente menor a 1)")
print(f"  1 > 1   → {1 > 1}  (1 no es estrictamente mayor a 1)")
print(f"  2 <= 1  → {2 <= 1}  (2 no es menor ni igual a 1)")
print(f"  1 >= 2  → {1 >= 2}  (1 no es mayor ni igual a 2)")

# --- Uso práctico: comparar variables ---
print("\n" + "=" * 45)
print("   USO PRÁCTICO")
print("=" * 45)
nota = 3.5
aprueba = nota >= 3.0
print(f"  nota = {nota}")
print(f"  nota >= 3.0  → {aprueba}  ({'APROBADO' if aprueba else 'REPROBADO'})")

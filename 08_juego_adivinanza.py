# ============================================================
#   EJERCICIO 8: Juego de adivinanza de números (ejercicio creativo)
# ============================================================
# El programa elige un número secreto aleatorio entre 1 y 10
# usando el módulo random. El jugador debe adivinarlo.
#
# Conceptos que se practican:
#   • import random y random.randint()
#   • Bucle while True con break
#   • try / except para manejar entradas inválidas
#   • Contador de intentos
#   • Pistas "muy alto" / "muy bajo"
# ============================================================

import random  # módulo estándar para generar números aleatorios

def jugar():
    """Ejecuta una ronda completa del juego de adivinanza."""
    # random.randint(a, b) → número entero aleatorio, INCLUYE a y b
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("\n" + "=" * 45)
    print("¡JUEGO DE ADIVINANZA!")
    print("=" * 45)
    print("Estoy pensando en un número entre 1 y 10.")
    print("¿Puedes adivinarlo?\n")

    while True:
        # try/except captura errores si el usuario escribe letras
        try:
            adivinanza = int(input("Tu adivinanza: "))
            intentos += 1  # incrementamos el contador en cada intento

            if adivinanza < numero_secreto:
                print("  ↑ Demasiado bajo. Intenta con un número mayor.")
            elif adivinanza > numero_secreto:
                print("  ↓  Demasiado alto. Intenta con un número menor.")
            else:
                # El usuario acertó → salir del bucle
                print(f"\n  🎉 ¡Felicidades! Adivinaste el número {numero_secreto}")
                print(f"  Lo lograste en {intentos} {'intento' if intentos == 1 else 'intentos'}.")
                break

        except ValueError:
            # Se ejecuta si int() no puede convertir la entrada
            print("  ⚠  Por favor ingresa un número entero válido.")

# --- Bucle principal: permite jugar varias rondas ---
while True:
    jugar()
    otra = input("\n  ¿Quieres jugar otra vez? (si / no): ")
    if otra.strip().lower() != "si":
        print("\n  ¡Hasta la próxima! 👋")
        break

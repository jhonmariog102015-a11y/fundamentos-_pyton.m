# ============================================================
#   ARCHIVO 20: Actividad de Conjuntos (Sets)
# ============================================================
# Este archivo aplica la teoría de conjuntos para gestionar
# inscripciones. Utiliza operaciones lógicas como unión,
# intersección y diferencia para identificar aprendices en
# múltiples cursos y eliminar registros duplicados.
# ============================================================
# 1. Definición de conjuntos
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

# 2. Operaciones de conjuntos
# Unión triple: total de aprendices únicos
total_aprendices = python_curso | java_curso | bd_curso
print(f"Total de aprendices únicos: {total_aprendices}")

# Intersección: Python Y Java
python_y_java = python_curso & java_curso
print(f"Aprendices en Python y Java: {python_y_java}")

# Diferencia: Solo Python (no Java ni BD)
solo_python = python_curso - (java_curso | bd_curso)
print(f"Aprendices solo en Python: {solo_python}")

# Exactamente dos programas (Lógica: (P&J | J&B | B&P) - (P&J&B))
inter_pj = python_curso & java_curso
inter_jb = java_curso & bd_curso
inter_bp = bd_curso & python_curso
inter_triple = python_curso & java_curso & bd_curso

exactamente_dos = (inter_pj | inter_jb | inter_bp) - inter_triple
print(f"Aprendices en exactamente dos programas: {exactamente_dos}")

# 3. Determinar inscritos únicos desde una lista
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']
unicos_inscritos = set(inscripciones)
print(f"Se inscribieron {len(unicos_inscritos)} aprendices únicos: {unicos_inscritos}")

# 4. Diccionario de conteo por comprensión
# Contamos en cuántos sets aparece cada nombre de la unión total
conteo_programas = {
    nombre: sum(nombre in curso for curso in [python_curso, java_curso, bd_curso])
    for nombre in total_aprendices
}
print(f"Conteo de programas por aprendiz: {conteo_programas}")

# 5. Bonus: Matriculados en los tres programas
en_todos = python_curso & java_curso & bd_curso
print(f"Aprendices en los tres programas: {en_todos if en_todos else 'Ninguno'}")
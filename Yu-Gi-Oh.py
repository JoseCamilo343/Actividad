import random

# --- Generar mazo completo de 52 cartas ---
def generar_mazo():
    """Función para construir un mazo estándar de póker con su respectivo color."""
    palos = {'c': 'RED','c':'BLACK','t': 'RED', 't': 'BLACK','d': 'BLACK', 'd':'RED','p': 'BLACK', 'p':'RED'}  # c: corazones,++++ d: diamantes, t: tréboles, p: picas
    valores = list(range(1,14))  # Valores de 1 (As) hasta 13 (Rey)
    mazo = []
    for palo, color in palos.items():
        for valor in valores:
            mazo.append((valor,palo,color))  # Cada carta representada por tupla
    random.shuffle(mazo)  # Aleatorizar orden
    return mazo

# --- Definir criterio de ordenamiento para cartas ---
def bubble(carta):
    valor, palo, color = carta
    orden_palos = {"c": 0, "t": 1, "d": 2, "p": 3}   # Jerarquía definida para palos
    orden_colores = {"RED": 0, "BLACK": 1}          # Jerarquía definida para colores
    return (orden_colores[color], orden_palos[palo], valor)

# --- Algoritmo burbuja aplicado al mazo ---
def bubble_mazo(mazo):
    # Recorre y compara cartas adyacentes hasta ordenar por el criterio definido
    n = len(mazo)
    for i in range(n):
        for j in range(0, n-i-1):
            if bubble(mazo[j]) > bubble(mazo[j+1]):
                # Intercambio de posiciones (swap)
                mazo[j], mazo[j+1] = mazo[j+1], mazo[j]
    return mazo

# --- Visualización del mazo en formato legible (traductor de ordenamiento) ---
def mostrar_mazo(mazo):
    return [f"{valor}{palo}({color})" for valor, palo, color in mazo]

# --- Proceso principal ---
mazo_desordenado = generar_mazo()
print(f"\nBaraja desordenado: {mostrar_mazo(mazo_desordenado)}")
print(f"\nNumero de cartas en el mazo: {len(mazo_desordenado)}")

# Selección de 13 cartas iniciales (simulación de mano)
seleccion_mazo = mazo_desordenado[:13]
print(f"\nCartas seleccionadas (13 desordenadas): {mostrar_mazo(seleccion_mazo)}")

# Ordenamiento de las cartas seleccionadas
mazo_ordenado = bubble_mazo(seleccion_mazo)
print(f"\nCartas ordenadas:                       {mostrar_mazo(mazo_ordenado)}")
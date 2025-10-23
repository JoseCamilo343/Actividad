import requests
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.evoluciones = [] 
class Grafo:
    def __init__(self):
        self.lista_adyacencia = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.lista_adyacencia:
            self.lista_adyacencia[nombre] = []

    def agregar_arista(self, origen, destino):
        self.lista_adyacencia[origen].append(destino)

    def mostrar(self):
        print("\n Cadena de evolución ")
        for nodo, vecinos in self.lista_adyacencia.items():
            print(f"{nodo} {vecinos}")
# Funcion
def construir_grafo(chain, grafo):
    nombre_actual = chain["species"]["name"]
    grafo.agregar_nodo(nombre_actual)
    if not chain["evolves_to"]: 
        return
    for evolucion in chain["evolves_to"]:
        nombre_evo = evolucion["species"]["name"]
        grafo.agregar_nodo(nombre_evo)
        grafo.agregar_arista(nombre_actual, nombre_evo)
        construir_grafo(evolucion, grafo)  

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False
# Menu
print("\n Pokémon en la cadena de evolución \n")
nombre_pokemon = input("Escribe el nombre del Pokémon que deseas buscar: ").strip().lower()
url_pokemon = f"https://pokeapi.co/api/v2/pokemon-species/{nombre_pokemon}/"
respuesta = requests.get(url_pokemon)
if respuesta.status_code != 200:
    print("Pokémon no encontrado. Verifica el nombre.")
else:
    datos_pokemon = respuesta.json()
    url_cadena = datos_pokemon["evolution_chain"]["url"]
    respuesta_cadena = requests.get(url_cadena)
    if respuesta_cadena.status_code != 200:
        print("Error al obtener la cadena de evolución.")
    else:
        datos_cadena = respuesta_cadena.json()
        cadena = datos_cadena["chain"]
        grafo = Grafo()
        construir_grafo(cadena, grafo)
        grafo.mostrar()
        pokemones = sorted(grafo.lista_adyacencia.keys())
        print("\nPokémon en la cadena de evolución ordenados:")
        print(pokemones)
        encontrado = busqueda_binaria(pokemones, nombre_pokemon)

        print("\n Resultado de la búsqueda:")
        if encontrado:
            print(f"El Pokémon '{nombre_pokemon}' SÍ pertenece a esta cadena de evolución.")
        else:
            print(f"El Pokémon '{nombre_pokemon}' NO pertenece a esta cadena de evolución.")
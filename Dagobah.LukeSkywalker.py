import requests

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

class Grafo:
    def __init__(self):
        self.nodos = {}
    def agregar(self, origen, destino):
        if origen not in self.nodos: self.nodos[origen] = Nodo(origen)
        if destino not in self.nodos: self.nodos[destino] = Nodo(destino)
        self.nodos[origen].vecinos.append(destino)
    def mostrar(self):
        print("\nUbicaciones:")
        for nombre in self.nodos:
            print(f"{nombre} {self.nodos[nombre].vecinos}")

def geocodificar(lugar):
    url = f"https://nominatim.openstreetmap.org/search?q={lugar},Colombia&format=json"
    respuesta = requests.get(url, headers={'User-Agent':'Mozilla/5.0'}).json()
    return (respuesta[0]['lon'], respuesta[0]['lat']) if respuesta else None

def calcular_ruta(origen, parada, destino):
    puntos = [geocodificar(origen)]
    if parada:
        puntos.append(geocodificar(parada))
    puntos.append(geocodificar(destino))
    if None in puntos:
        return None

    coordenadas = ";".join([f"{lon},{lat}" for lon, lat in puntos])
    url = f"http://router.project-osrm.org/route/v1/driving/{coordenadas}?overview=false&steps=true"
    respuesta = requests.get(url).json()
    if "routes" not in respuesta:
        return None
    
    def sumar_distancias(indice=0):
        rutas = respuesta["routes"][0]["legs"]
        return 0 if indice == len(rutas) else rutas[indice]["distance"] + sumar_distancias(indice + 1)
    
    def sumar_tiempos(indice=0):
        tramos = respuesta["routes"][0]["legs"]
        return 0 if indice == len(tramos) else tramos[indice]["duration"] + sumar_tiempos(indice + 1)

    distancia_km = sumar_distancias() / 1000
    tiempo_segundos = sumar_tiempos()
    return distancia_km, tiempo_segundos 

def busqueda_binaria(lista, valor, inicio=0, fin=None):
    fin = len(lista) - 1 if fin is None else fin
    if inicio > fin:
        return False
    medio = (inicio + fin) // 2
    if lista[medio] == valor:
        return True
    elif lista[medio] < valor:
        return busqueda_binaria(lista, valor, medio + 1, fin)
    else:
        return busqueda_binaria(lista, valor, inicio, medio - 1)
# Menu
print("\n Escriba tu ruta de viaje en Colombia:")

origen = input("\nIngrese el Origen: ")
parada = input("\nIngrese la Parada: ")
destino = input("\nIngrese el Destino: ")
resultado = calcular_ruta(origen, parada, destino)

if resultado:
    distancia_total, tiempo_total = resultado
    horas = int(tiempo_total // 3600)
    minutos = int((tiempo_total % 3600) // 60)

if distancia_total:
    grafo_ruta = Grafo()
    grafo_ruta.agregar(origen, parada if parada else destino)
    grafo_ruta.agregar(parada if parada else origen, destino)
    grafo_ruta.mostrar()

    lugares = sorted([origen, parada, destino])
    busqueda_binaria(lugares, origen)

    print(f"\nRuta: {origen} , {parada if parada else '(sin parada)'} , {destino}")
    print(f"Distancia total: {distancia_total} km")
    print(f"Tiempo estimado de viaje: {horas} horas y {minutos} minutos")
else:
    print("\nNo se pudo calcular la ruta.")
import requests

def busqueda_binaria(lista, objetivo):
    """
    Busca un objetivo en una lista ordenada usando el algoritmo binario.
    Retorna el índice del objetivo o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio  # ¡Encontrado!
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # No se encontró el objetivo

def busqueda_lineal(lista, objetivo):
    """
    Busca un objetivo en una lista usando el algoritmo lineal.
    Retorna el índice del objetivo o -1 si no se encuentra.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # ¡Encontrado!
    return -1  # No se encontró el objetivo


def main():
    # Consumir la API de países de Europa
    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    data = response.json()

    # Crear la lista de los nombres de países
    paises = [country["name"]["common"] for country in data]
    paises.sort()

    # Guardar un diccionario para acceder rápido a la informacion
    pais_info = {country["name"]["common"]: country for country in data}

    # Preguntar tipo de búsqueda
    print("Seleccione el tipo de búsqueda:")
    print("1. Lineal")
    print("2. Binaria")
    opcion = input("Opción: ")

    # Nombre del país a buscar
    buscado = input("Ingrese el nombre del país a buscar: ")

    # Ejecutar la búsqueda según la opción elegida
    if opcion == "1":
        indice = busqueda_lineal(paises, buscado)
    elif opcion == "2":
        indice = busqueda_binaria(paises, buscado)
    else:
        print("Opción no válida.")
        return

    # Mostrar resultados
    if indice != -1:
        pais = paises[indice]
        url_mapas = pais_info[pais]["maps"]["googleMaps"]
        print(f"\nNombre: {pais}")
        print(f"Google Maps: {url_mapas}")
    else:
        print(f"\nEl país '{buscado}' no se encuentra en la lista.")

if __name__ == "__main__":
    main()
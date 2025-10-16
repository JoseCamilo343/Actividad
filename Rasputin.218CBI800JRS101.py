digitos = []
# Función para sumar los dígitos
def suma_digitos(n):
    if n < 10:
        digitos.append(n) 
        return n
    else:
        ultimo = n % 10
        digitos.append(ultimo)
        resto = n // 10         
        return ultimo + suma_digitos(resto)
# Programa principal
def main():
    print(" Suma de los digitos de numeros enteros (*---positivos---*)")
    n = int(input("Ingresa un número entero positivo: "))
    if n < 0:
        print("Por favor, ingresa un número positivo.")
    else:
        total = suma_digitos(n)
        digitos.reverse()  
        print("\nDígitos encontrados:", digitos)
        print("La suma de los dígitos es:", total)
main()
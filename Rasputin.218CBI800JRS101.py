def sumar(a, b):
    if b == 0:
        return a
    else:
        return sumar(a + 1, b - 1)
def restar(a, b):
    if b == 0:
        return a
    else:
        return restar(a - 1, b - 1)
def multiplicar(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicar(a, b - 1)
def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    if a < b:
        return 0
    else:
        return 1 + dividir(a - b, b)
operaciones = [
    [1, "Sumar", sumar], [2, "Restar", restar], [3, "Multiplicar", multiplicar], [4, "Dividir", dividir]]
def menu():
    while True:
        print("\n CALCULADORA ")
        for option in operaciones:
            print(f"{option[0]} {option[1]}")
        print("5. Salir"); Elige = input("Elige una opción : ")
        if Elige == "5": 
            print("Gracias por usar la calculadora.")
            break
        if Elige in ["1", "2", "3", "4"]: 
            a = int(input("Número a: ")); b = int(input("Número b: ")); indice = int(Elige) - 1; funcion = operaciones[indice][2]; print("Resultado =", funcion(a, b))
        else: 
            print("Opción no valida, porfavor intentalo de nuevo.")
menu()
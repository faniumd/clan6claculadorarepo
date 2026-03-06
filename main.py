# main.py - Sprint 1 calculadora
def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def solicitar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def main():
    operaciones_realizadas = 0
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2"]:
            num1 = solicitar_numero("Ingrese el primer número: ")
            num2 = solicitar_numero("Ingrese el segundo número: ")

            if opcion == "1":
                resultado = sumar(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcion == "2":
                resultado = restar(num1, num2)
                print(f"Resultado: {resultado}")

            operaciones_realizadas += 1

        elif opcion in ["3", "4"]:
            print("Función multiplicar/dividir pendiente...")  # Sprint 2
        elif opcion == "5":
            print(f"Gracias por usar la calculadora. Total operaciones: {operaciones_realizadas}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

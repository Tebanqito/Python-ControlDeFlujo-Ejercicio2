numero_inicial = int(input("Ingrese el numero inicial: "))
numero_final = int(input("Ingrese el numero final: "))

while(numero_final < numero_inicial):
    print("El numero final no puede se menor al numero inicial")
    numero_final = int(input("Por favor ingrese el numero final nuevamente: "))

for numero in range(numero_inicial, numero_final):
    if(numero % 2 != 0):
        print(numero)

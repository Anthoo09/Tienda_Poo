#  Mostrar los múltiplos de 3 del 3 al 30 usando un bucle for


for numero in range(3, 31, 3):
    print(f"Número: {numero}")

# WHILE: Pedir números al usuario y sumarlos hasta que escriba 0

Suma_T = 0
numero = None
contador = 0


while numero !=0:
    numero = int(input("INTRODUCE EL NUMERO 0 PARA TERMINAR:"))
    if numero !=0:
        Suma_T += numero
        contador +=1

print(f"LA SUMA TOTAL ES: {Suma_T}")
print(f"Números introducidos (sin contar el 0): {contador}")


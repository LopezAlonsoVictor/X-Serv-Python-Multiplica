#!/usr/bin/python3

numeros = list(range(1,11))

for operando1 in numeros:
    print("Tabla del ",operando1)
    for operando2 in numeros:
        aux = operando1*operando2
        print(operando1, "por", operando2, "es", aux)
    print("\n")

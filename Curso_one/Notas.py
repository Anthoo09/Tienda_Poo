nota = int(input("Ingresa tu calificacion: "))
if nota < 7:
    print(f"SACASTE UN {nota}: REPROBASTE")
elif nota >= 7 and nota < 9:
    print(f"SACASTE UN {nota}: APROBASTE")
else:
    print(f"SACASTE UN {nota}: ¡EXCELENTE ESTUDIANTE!")

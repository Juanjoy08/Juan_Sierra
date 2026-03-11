print("Calificación final del estudiante")
Nombre= input("ingrese nombre del estudiante:")
print(f"hola:{Nombre}")

Nota_1= input("ingrese nota 1 del estudiante: ")
Nota_2= input("ingrese nota 2 del estudiante: ")
Nota_3= input("ingrese nota 3 del estudiante: ")
Nota_4= input("ingrese nota 4 del estudiante: ")
Nota_5= input("ingrese nota 5 del estudiante: ")

suma_de_notas= int(Nota_1) + int(Nota_2) + int(Nota_3) + int(Nota_4) + int(Nota_5)
Nota_definitiva= suma_de_notas/5
print(f"la nota definitiva es: {Nota_definitiva}")

if Nota_definitiva >= 60:
    print("Aprobado")
elif Nota_definitiva >= 40:
    print("En recuperación")
else :
    print("Reprobo")


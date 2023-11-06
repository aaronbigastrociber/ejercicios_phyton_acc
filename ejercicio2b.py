# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)
def esMayorEdad(e):
    if e>=18 :
        return True
    else:
        return False
    

# Programa principal
def main():
    nombre="Mariano";
    edad=19;

    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...
    if esMayorEdad(edad):
        print("Usted es mayor de edad")
    else:
        print("Todavia eres menor de edad")

if __name__== "__main__" :
   main()

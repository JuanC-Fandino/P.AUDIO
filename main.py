from Furierr import Square
from archivar import Archivo
from dos import Sierra

def main():

    print ("Generador de Ondas \nV 1.0 \n")

    opcion = input("Ingrese el numero correspondien segun el tipo de Onda que desea generar:\n1.Sierra\n2.Cuadrada\n3.Triangular\n")

    if opcion==1:

        print ("Ingrese los parametros: ")
        Tono = input("Ingrese la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
        MaxBits = input("Ingrese el numero de bits: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
        Nombre = (Nombre + ".wav")

        onda = Sierra(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        datos = onda.generar()

        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datos)

        onda.graficar(datos)

    elif opcion==2:

        print ("Ingrese los parametros: ")
        Tono = input("Ingrese la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
        MaxBits = input("Ingrese el numero de bits: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
        Nombre = (Nombre + ".wav")
        print(Frecuenciadesampleo)


        onda = Square(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        datos = onda.generar()


        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datos)

        onda.graficar(datos)

    elif opcion==3:

        print("Aun no configurada")

    else:
        print("Opcion no valida")





if __name__ == "__main__":
    main()

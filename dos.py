import math
import matplotlib.pylab as plt

class Sierra:
        wavearray = []



        def __init__(self, frecuencia, sampling, bits, time):

            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time
            self.omega = 2*math.pi*frecuencia
            self.valorinicial = 0
            self.valorfinal = 2
            self.contador = (2-0)/float(sampling)
            self.amplitud = ((2**bits)/2)

        def generar(self):

            print self.contador

            for i in range(0, self.tamano):

                for n in range(1,20):

                    tiempo = 0

                    for x in range(0, self.SamplingRate):


                        datos = (self.amplitud/(n*math.pi*self.Frecuencia))*math.sin(n*self.omega*tiempo)
                        #print datos
                        tiempo += self.contador

                    Sierra.wavearray.append((self.amplitud/2*self.Frecuencia)-datos)






            return Sierra.wavearray



        def graficar(self, array):
                plt.plot(array, color="green", linewidth=1.0, linestyle="-")
                plt.show()
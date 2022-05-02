#Ejercicio 1 Dada la siguiente clase, identificá la interfaz y el estado de la misma:
'''
La interfaz es alimento y caricias y el estado es energia, comer, acariciar y estaDebil
'''
#Ejercicio 2 Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar 
# si al hacerlo la energía toma el valor 0 o valor negativo.

def volar(self, kms):
    if self.energia <= 0:
        return False
    else:
        self.energia -= 10 + kms 

#Ejercicio 3 Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un 
# descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver 
# cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos 
# casos aplicar este descuento.

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def descuento(self, porcentaje):
        desc = self.precio * porcentaje / 100
        return self.precio - desc

#Ejercicio 4 Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar 
# directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
'''
inc()
dis()
reset()
valorActual()
valorNuevo(nuevoValor)
Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.
'''
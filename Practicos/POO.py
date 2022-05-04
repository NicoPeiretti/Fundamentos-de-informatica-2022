#Parte 1 POO:

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
class Contador:
    def __init__(self, valor):
        self.valor = valor

    def inc(self):
        self.valor += 1
    
    def dis(self):
        self.valor -=  - 1

    def reset(self):
        self.valor *= 0

    def valorActual(self):
        return self.valor

    def valorNuevo(self, nuevoValor):
        self.valor == nuevoValor

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()

#Ejercicio 5:
class Contador:
    def __init__(self, valor):
        self.valor = valor
        self.comando = ''

    def inc(self):
        self.valor += 1
        self.comando = 'incrementa'
    
    def dis(self):
        self.valor -=  - 1
        self.comando = 'disminuye'

    def reset(self):
        self.valor *= 0
        self.comando = 'reset'

    def valorActual(self):
        return self.valor

    def valorNuevo(self, Valor):
        self.valor == Valor
        self.comando = 'actualiza'

    def ultimoComando(self):
        print(self.comando)

#Ejercicio 6:
class Calculadora:
    def cargar(self, numero):
        self.numero = numero

    def sumar(self, suma):
        self.numero += suma

    def restar(self, resta):
        self.numero -= resta

    def multiplicar(self, multiplicador):
        self.numero *= multiplicador

    def ValorActual(self):
        return self.numero

#Ejercicio 7:
class Gorriones:
    def __init__(self):
        self.gramos = 0
        self.kms = 0
        self.vuelos = []
        self.comidas = []

    def volar(self, kms):
        self.kms += kms
        self.vuelos.append(kms)

    def comer(self, gramos):
        self.gramos += gramos
        self.comidas.append(gramos)

    def CSS(self):
        if self.gramos <= 0:
            return None
        else:
            return self.kms/self.gramos
    
    def CSSP(self):
        if self.gramos <= 0:
            return None
        else:
            return int(max(self.vuelos))/int(max(self.comidas))
    
    def CSSV(self):
        if self.gramos <= 0:
            return None
        else:
            return len(self.vuelos)/len(self.comidas)
    
    def enEquilibrio(self):
        if (0.5 < self.CSS() < 2):
            return True
        else:
            False

#Parte 2 POO:
class Perro:
   def __init__(self):
        self.alimento = 0
        self.caricias = 0
   def energia(self):
        return self.alimento + (self.caricias * 10)

   def comer(self, gramos):
        self.alimento += gramos

   def alimento(self):
	    print(self.alimento)
        
   def acariciar(self):
        self.caricias += 1

   def estaDebil(self):
        return self._caricias < 2

   def pasear(self, km):
	    self.alimento -= km / 4

class Gato:
   def __init__(self):
        self.alimento = 0
        self.caricias = 0

   def energia(self):
        return self.alimento + (self.caricias * 8)

   def comer(self, gramos):
        self.alimento += gramos * 1.5

   def caricias(self):
	    print(self.caricias)
        
   def acariciar(self):
        self.caricias += 1
        
   def estaDebil(self):
        return self.caricias < 4


''''
Las interfaces son alimento y caricias, los estados son energia, comer, alimento, acariciar, estaDebil y pasear. 
Si comparten interfaz y son polimorficas
'''   

#Ejercicio 2:

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def estaEnEquilibrio(self):
      return 150 < self.energia < 300

#Ejercicio 3:




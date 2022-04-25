#DESAFIO 1c
'''
#Paso 9) Verificar si el mate tiene agua
#momento decisivo:
#paso 10) Si no tiene agua, buscar una pava y calentar el agua, vertirla y disfruta de tu mate
#Paso 11) si tiene agua, disfrutar del mate
'''
'''
#DESAFIO 2
#El prompt de ambas es el mismo. 
#El lenguaje es python.
'''
#Desafio 3
"""saludo = "Hola mundo"_ al invocarlo no devuelve nada ya que se está creando una nueva variable pero... 
Al correr `len(saludo)` te devuelve la cantidad de caracteres en el saludo= "Hola mundo". 
Luego `saludo.upper()` te devuelve el string en mayúsculas, mientras que `saludo.lower()` en minúsculas. 
En `saludo.count("o")` te dice la cantidad de veces que la letra "o" se repite en el saludo."""

#Desafio 4
'''Al probar `saludo.replace("mundo", "terricolas")` reemplaza "mundo" por "terricolas"'''

#Desafio 5

#DESAFIO 6
def termos_por_ronda(personas): 
    return (personas * 30) / 1000

#DESAFIO 7
def vaquita(costos, comensales):
    return costos / comensales

#DESAFIO 8
termo = 1000
def calcular_cantidad_de_agua(personas): 
    if termo >= (personas * 30): 
        return personas * 30
    else:
        return "Necesitas mas de un termo"

#DESAFIO 9
def empanadas_por_gusto():
    for i in lista_comensales:
        print(pedido[i])

gustos = {"no_veggie": 0, "veggie": 0} # iniciar un contador para cada gusto
pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
lista_comensales = ["Ana", "Paul", "Luz"]
def empanadas_por_gusto(): 
    for comensal in lista_comensales: 
        gustos[pedido[comensal]] += 1 # del gusto que sea sumame 1
    # si usas if lo tenés que hacer para cada gusto y no estaría del todo ok 
    
print(gustos)
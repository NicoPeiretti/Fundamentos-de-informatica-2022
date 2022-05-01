# EJERCICIO 1 (condicionales)
string = input("Ingrese una palabra o una frase: ")
cap = string.capitalize() #sino puedo usar str.isupper[0]
if string == cap: 
  print("la primer letra es mayúscula.")
else: 
  print("la primer letra es minúscula")

# EJERCICIO 2 (condicionales)
numero = int(input("Ingrese un número: "))
if numero > 0: 
  print("es positivo")
  if numero%2 == 0: 
    print("es par")
  else: 
    print("es impar")
elif numero < 0: 
  print("es negativo")
  if numero%2 == 0: 
    print("es par")
  else: 
    print("es impar")
else: 
  print("es cero y par")

# EJERCICIO 3 (condicionales)
num = int(input("Escribí un número del 1 al 6: "))
if  num >= 1 or num <= 6: 
  print("la cara opuesta del dado es: " + str(7 - num))
else: 
  print("el número ingresado es incorrecto") 

# EJERCICIO 4 (condicionales)
peso_paquete = int(input("Ingrese el peso del paquete: "))
lugar = input("Ingrese la ubicación de la entrega: ")
costos_ubicacion = {"America del sur": "10usd", "America central": "15usd", "America del norte": "18usd", "Europa": "24usd", "Asia": "30usd"}
if peso_paquete <= 5: 
  print("el cobro por entrega es " + costos_ubicacion[lugar])  
else: 
  print("su entrega fue rechazada, no puede transportarse por exceso de peso")

# EJERCICIO 5 (condicionales)
num_dia = int(input("Ingrese el número del día del 1 al 7: "))
dias_semana = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6:"Sábado", 7:"Domingo"}
if num_dia > 7 or num_dia < 1: 
  print("el número ingresado es inválido, intentelo nuevamente")
else: 
  print(dias_semana[num_dia])

# EJERCICIO 6 (listas)
lista = [input(), input(), input(), input(), input()]
lista_invertida = [lista[4], lista[3], lista[2], lista[1], lista[0]] #chequear por qué no se puede lista[-1]
print(lista_invertida)
#el [::-1] funciona para invertir todos los elementos de la lista

# EJERCICIO 7 (listas)
numero = int(input("Ingrese un número: "))
lista_num = [] 
while numero >= 0:
  lista_num.append(numero)
print(lista_num)

# EJERCICIO 8 (listas)
Lista1 = [int(input("ingrese 5 numeros, uno por linea: ")), int(input()), int(input()), int(input()), int(input())]
Lista2 = [int(input("ingrese 5 numeros nuevamente: ")), int(input()), int(input()), int(input()), int(input())]
Lista3 = [Lista1[0]+Lista2[0], Lista1[1]+Lista2[1], Lista1[2]+Lista2[2], Lista1[3]+Lista2[3], Lista1[4]+Lista2[4]]
print(Lista3)

# EJERCICIO 9 (listas)
lista_nombre = []
lista_edad = []
nombre = input('ingrese el nombre del alumno: ')
edad = input('ingrese la edad del alumno: ')
while nombre != "*":
    lista_nombre.append(nombre)   
    lista_edad.append(edad)
    nombre = input('ingrese el nombre del alumno: ')
    if nombre == "*":
        continue
    edad = input('ingrese la edad del alumno: ')
print("la edad máxima de los alumnos es: " + max(lista_edad))
dic = {"lista_nombre" : "lista_edad"} 

# EJERCICIO 10 (diccionarios)
contadores = {} 
cadena = input("Escribí una cadena de caracteres: ") 
for caracter in cadena: 
  contadores[caracter] += 1
else: 
  contadores[caracter] = 1

for clave, valor in contadores.items(): 
  print(clave, valor)

# EJERCICIO 11 (diccionarios)
contadores = {} 
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper(): 
  contadores[letra] = 0

cadena = input("Escribí una cadena de caracteres: ")

for caracter in cadena: 
  if caracter.lower() in alfabeto: 
    contadores[caracter] += 1

for campo, valor in contadores.items(): 
  print (campo, valor)

# EJERCICIO 12 (diccionarios)
cantidad = int(input("Introducir cantidad de alumnos: "))
alumnos = {} 

for numero in range(cantidad): 
  alumno = input("alumno: ")
  notas = [] 
  nota = int(input("nota: "))
  while nota >= 0:
    notas.append(nota)
    nota = int(input("nota: "))
  alumnos[alumno] = notas 

for alumno in alumnos: 
  print(alumno, sum(alumnos[alumno]) / len(alumnos[alumno])) 

# EJERCICIO 13 (funciones)
n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese el otro número: '))

def esMultiplo(n1, n2): 
  if (n1%n2) == 0: 
    print(str(n1) + ' es múltiplo de ' + str(n2)) 
  if (n2%n1) == 0: 
    print(str(n2) + ' es múltipo de ' + str(n1))
  else: 
    print('Los números que ingresaste no son múltiplos entre sí')

# EJERCICIO 14 (funciones)
def temperatura_media(temperatura_max, temperatura_min):
  media = int((temperatura_max) + int(temperatura_min))/2
  print('La temperatura media es ', media, 'grados')

dias = int(input('Ingrese la cantidad de dias: '))
contador = 0 
while contador < dias:
    max = int(input('Ingrese la temperatura maxima: '))
    min = int(input('Ingrese la temperatura minima: '))
    temperatura_media(max, min)
    contador += 1
# EJERCICIO 15 (funciones)
socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}
print('socios_activos: ' + str(len(socios_activos)))
numero_de_socio = int(input('Ingrese el numero del socio: '))
print(socios_activos[numero_de_socio][2])
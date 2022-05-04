#Ejercicio 1:
import re
def caracter_permitido(string):
    return re.search('\w', string)
#Ejercicio 2:
import re
def caracter_no_permitido(string):
    return re.search('\W', string)

#Ejercicio 3:
import re
texto = input('Inserte su texto: ')
patern1 = 'he?'
patern2 = 'he+'
patern3 = 'he{2,3}'

def verificar(texto): 
    cond1 = re.search(patern1, texto)
    cond2 = re.search(patern2, texto)
    cond3 = re.search(patern3, texto)
    if cond3 is None: 
        if cond2 is not None:
            print('Se cumplieron las dos condiciones primeras')
        elif cond1 is not None: 
            print('Se cumplió sólo la condición primera')
        else:
            print('No se cumplió ninguna condición')
    else: 
        print('Se cumplieron las tres condiciones!') 

verificar(texto)

#Ejercicio 4:
import re
def funcion_4(string):
    return re.search('\w_\w', string)

#Ejercicio 5:
import re
def numero_especifico(string):
    return re.search

#Ejercicio 6:
import re
def funcion_6(strings, frase):
    for palabra in strings:
        if re.search(palabra, frase) is not None:
            print('La palabra', palabra, 'esta en la frase')
        else:
            print('La palabra', palabra, 'no esta en la frase')

strings = ['hola', 'como', 'estas', 'pa']
frase = 'hola como estas pa'
funcion_6(strings, frase)

#Ejercicio 7:
import re
string = input('Inserte el string: ')
def funcion_7(string):
    if re.search('\w\s', string):
        print('Cumple las condiciones')
    else:
        print('No cumple las condiciones')

#Ejercicio 8:
import re

input('Ingrese un string: ')
lista_numero = []
patron = '\d+'
def funcion_8(string):
    for numero in string:
        re.findall(patron, string)
        lista_numero.append(numero)
        print(lista_numero)

#Ejercicio 9:
import re
def funcion_9(string):
    return re.sub('-(.*?)-', '', string)

print(funcion_9("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))
    
#Ejercicio 10:

#Ejercicio 11:
import re
patron = "(P\w*)\s(P\w*)"
def funcion_11(lista):
    for string in lista:
        coincidencia = re.search(patron, string)
        if coincidencia is not None:
            print(coincidencia.group())

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
funcion_11(lista)

#Ejercicio 12:
import re
def funcion_12(string):
    return re.sub(r'[\s_:]', '|', string)

string = 'hola papa como estas'
print(funcion_12(string))

#Ejercicio 13:
import re
def funcion_13(string):
    return re.sub(r'\D', '_', string, 2)

string = '+++Que hace pibe'
print(funcion_13(string))



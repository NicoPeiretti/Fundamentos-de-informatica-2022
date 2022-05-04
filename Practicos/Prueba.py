import re
patron = "(P\w*)\s(F\w*)"
def funcion_11(lista):
    for string in lista:
        coincidencia = re.search(patron, string)
        if coincidencia is not None:
            print(coincidencia.group())

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
funcion_11(lista)
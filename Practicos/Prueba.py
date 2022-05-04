import re
string = input("escriba algo: ")
patron = '\d{0,}'
def funcion_8(string):
    for patron in string:
        return re.findall(patron, string)

print(funcion_8(string))
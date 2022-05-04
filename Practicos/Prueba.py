import re
def funcion_14(string):
    return re.sub(r'[\s]', ';', string)
    
print(funcion_14('hola  mi nombre es    Nicolas Peiretti'))
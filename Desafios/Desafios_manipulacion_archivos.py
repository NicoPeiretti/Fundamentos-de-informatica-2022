# Desafio 1:
archivo = open('bio.txt', 'a')
archivo.close()

#Desafio 2:
'''
os.mkdir() : Crea una carpeta nueva
os.listdir() : Lista los archivos de la biblioteca 

'''

#Desafio 3:
with open('bio.txt', 'w') as miarch:
    miarch.write('Nicolas Peiretti, 19 años')

#Desafio 4:
leer_archivo = open('manipulacion_archivos.txt', 'r')
leer_archivo.readlines()

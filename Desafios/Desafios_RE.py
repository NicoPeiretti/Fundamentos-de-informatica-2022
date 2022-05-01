#Desafio 1: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
import re
'\d{4,}'

#Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
import re
'[a-z]{3,6}'

#Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
import re
'ab*'

#Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
#texto = 'En la clase de Introducción a la programación hay 30 estudiantes'
'\d+'

#Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 ¿Qué resultado obtenés? ¿Qué quiere decir el mensaje span?
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = '{22,26}'
re.search(patron, texto)

#Desafio VI: Expresá el patron de búsqueda utilizando lo visto anteriormente sobre metacaracteres y rangos.
import re


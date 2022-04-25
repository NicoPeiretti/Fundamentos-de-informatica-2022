import re
#Ejercicio 1:
string = 'eidjncjdenjvfjvb1234'
re.search('\w', string)

#Ejercicio 2:
import re
string = 'dkncdnj1324'
re.search('\W', string)

#Ejercicio 3:
import re
cadena = 'helena'
print(re.search('he(.*)', cadena))

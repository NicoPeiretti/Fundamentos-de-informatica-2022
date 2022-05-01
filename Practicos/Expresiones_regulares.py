#Ejercicio 1:
import re
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

#Ejercicio 4:
import re
string = "Defíni la función aprobar_materias"
patron = '\w' + '_' + '\w'
re.search(patron, string)

#Ejercicio 5:
import re
string = '093493niwonffonwodf'
re.search
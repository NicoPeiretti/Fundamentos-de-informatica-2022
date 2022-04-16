# EJERCICIO 1
def longitud(string): 
    return len(string)

# EJERCICIO 2
string = input("Ingrese una frase: ")
if len(string) >= 6: 
  print(str.upperstring[4:6])
else: 
  print("Su frase no tiene suficientes caracteres, por favor intente nuevamente")

# EJERCICIO 3
nombre_completo = input("Ingrese su nombre y apellido: ")
print("Hola ", nombre_completo)

# EJERCICIO 4
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
print(str.upper(nombre[0]), str.upper(apellido[0]), str.upper(apellido2[0]))

# EJERCICIO 5
def promedio_numeros(un_numero, otro_numero, ultimo_numero): 
  return (un_numero + otro_numero + ultimo_numero) // 3

# EJERCICIO 6
minutos = int(input("Ingrese una cantidad de minutos "))
print(minutos // 60, "horas y ", (minutos%60), " minutos")

# EJERCICIO 7
def sueldo(base, ventas): 
  comision = base * 0.1
  return base + (comision * ventas)

# EJERCICIO 8
def nota_final(respuestas): 
  resultado = 0 
  for respuesta in respuestas: 
    if respuesta == "correcta": 
      resultado += 4
    elif respuesta == "incorrecta": 
      resultado -= 1
    else: 
      resultado = resultado 
  return resultado 
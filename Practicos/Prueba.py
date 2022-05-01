socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}
print('socios_activos: ' + str(len(socios_activos)))
numero_de_socio = int(input('Ingrese el numero del socio: '))
print(socios_activos[numero_de_socio][2])

dar_de_baja = (input('Ingrese el nombre y apellido del socio que quiere dar de baja: '))
socios_activos.pop(dar_de_baja)[0]
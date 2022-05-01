# EJERCICIO 1 
with open('nombreArchivo', 'r') as file: 
    fileContent = file.readlines()

for fileline in fileContent: 
    noEmpiezaCon = 0 
    if not str.startswith(fileline, 'P'): 
        noEmpiezaCon += 1
    print(noEmpiezaCon) 

# EJERCICIO 2
with open('nombreArchivo', 'r') as file: 
    contentList = file.readlines()
    for i in range(len(contentList) + n), len(contentList):
        print(contentList[i])

# EJERCICIO 3
with open('nombreArchivo', 'r') as file: 
    contentList = file.readlines() 
    for i in range(len(contentList) - n), len(contentList): 
        print(contentList[i])

def read_n_back_lines(n, archivo): 
    texto = open(archivo, "r").readlines()
    for i in range((len(texto) -n), len(texto)):
        print(texto[i])
    texto.close()

# EJERCICIO 4
with open('nombreArchivo', 'r') as file: 
    fileContent = file.readlines()
    print(len(fileContent)) 

# EJERCICIO 5
with open('nombreArchivo', 'r') as file: 
    fileContent = file.readlines()

for fileline in fileContent: 
    fileline = fileline.replace('w', 'w \n')

with open('otroArchivo', 'a') as f: 
    for i in fileContent:
        f.write(i) 

# EJERCICIO 6 
with open('nombreArchivo', 'r') as file:
    fileContent = file.readlines()

for fileline in fileContent:
    fileline = fileline.remove('\n')

with open('otroArchivo', 'a') as f:
    for i in fileContent:
        f.write(i)

# EJERCICIO 7 
def palabra_mas_larga(archivo): 
    palabra = '' 
    max_long = 0
    with open(archivo, 'r') as f: 
        lista_palabra = f.read().split()
        for word in lista_palabra:
            if len(word) > max_long: 
                max_long = len(word)
    print(max_long) 

# EJERCICIO 8    

# EJERCICIO 9 
def word_counter(archivo): 
    frecuencias = dict() 
    with open(archivo, 'r') as miArchivo: 
        word_list = miArchivo.read().split() 
        for palabra in word_list:
            if palabra in frecuencias: 
                frecuencias[palabra] += 1
            else: 
                frecuencias[palabra] = 1 
        for word in frecuencias.keys(): 
            frecuencias[word] = round(frecuencias[word] / len(word_list),3) #3 decimales 
    print(frecuencias) 

# EJERCICIO 10 
def join_files(file1, file2, file3): 
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'a') as f3: 
        f3.write(f1.read() + f2.read())

join_files('documento1', 'documento2', 'documento3')
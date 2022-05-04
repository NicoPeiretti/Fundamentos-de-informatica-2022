def funcion_5(fileContent, letra):
    with open(fileContent, 'r') as file: 
        fileContent = file.readlines()
        for fileline in fileContent: 
            fileline = fileline.replace(letra, letra + '\n')
    with open(fileContent, 'a') as f: 
        for i in fileContent:
            f.write(i)

funcion_5('bio.txt', 'y')
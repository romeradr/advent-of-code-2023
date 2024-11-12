import re

def obtener_cuentas(linea):   
    ''' 
    Primero: obtener el número del juego de la string, toca buscar el número que va después del " "
    Segundo: separar la string por ";" para comparar por jugadas
    Tercero: calcular cada
    '''
    # linea = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green";

    jugadas = linea.split(";")
    game_number = jugadas[0].split(":")[0].split(" ")[1];

    # Ahora eliminamos el "Game X: " y tenemos sólo las jugadas
    jugadas[0] = jugadas[0].split(": ")[1]

    for jugada in jugadas:
        # Iteramos sobre cada jugada
        
        rgb = [0, 0, 0]

        words = jugada.split()

        for i, word in enumerate(words):        
            if word.isdigit() and "red" in words[i+1]:
                rgb[0] += int(word)
            elif word.isdigit() and "green" in words[i+1]:
                rgb[1] += int(word)
            elif word.isdigit() and "blue" in words[i+1]:
                rgb[2] += int(word)

        if rgb[0] > 12 or rgb[1] > 13 or rgb[2] > 14:
            return 0
    
    return int(game_number)     


f = open("input.txt", "r")

result = 0
for (line) in f.readlines():
    result += obtener_cuentas(line)

print(result)

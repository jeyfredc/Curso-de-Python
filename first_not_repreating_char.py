"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"d
"bcccccccccccccyb"y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {} #crea un diccionario, para posteriormente guardar letras que son "vistas o repetidas"

    for idx, letter in enumerate(char_sequence): #crea una especie de"conteo"en idx respecto a cada letra(letter) dentro de char_sequence
        if letter not in seen_letters:  #verifica que el valor para cada letra enla secuencia inicial NO este en seen_letters(letras repetidas)
            seen_letters[letter] = (idx, 1) #si es la primera vez que encuentra la letra, crea una tupla con valores de indice dela letra y cantidad de veces vista dentro del diccionario  con key dela letra,ej:  'a': (0, 2)
            print("solo te vi una vez")
            print(seen_letters)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1) #si no es la primera vez quela ve, entonces crea otra tupla donde agrega el valor del indice en el primer lugar y el valor de veces vista enla posicion 2, este valor va aumentando cada vez que ve una palabra repetida

    final_letters = [] #esta es la lista donde se guardaran las letras quese repiten una sola vez
    for key, value in seen_letters.iteritems(): #obtiene los valores de key y value dentro del diccionario para verificar el dato de numero de repeciones, este corresponde al value[1]
        if value[1] == 1:                       #si solo se repite la letra una vez 
            final_letters.append( (key, value[0]) )  #entonces lo agrega a la lista de final_letters 
   
    print("final_letters")
    print(final_letters)

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1]) #este se usa para ordenar la lista de final_letters de manera ordenada, ya los datos vienen desordenados desde seen_letters
    print("not_repeated_letters")
    print(not_repeated_letters)

    if not_repeated_letters: #si la lista de not_repeated_letters no esta vacia 
        print(not_repeated_letters[0])
        return not_repeated_letters[0][0]  #entonces retorna la posicion 0 dentro dela lista , y la posicion 0 dentro de esa tupla , ej: {('a',4),('b',6)}, en ese caso retorna a
    else:
        return '_' #si la lista de not_repeated_letters  esta vacia , es decir no hay caracteres repetidos, retorna '_'


if __name__ == '__main__':
    #programa que retorna caracteres no repetidos, si se repiten arroja el mensaje de todos los caracteres se repiten
    char_sequence = input('Escribe una secuencia de caracteres: ') #caracteres de entrada 

    result = first_not_repeating_char(char_sequence) 

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print(f'El primer caracter no repetido es: {result}')
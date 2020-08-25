import sys

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': '0'
}

def cypher(message): #Cifrar -- lo que se va a hacer es separar el mensaje que se ingresa por teclado
    words = message.split(' ') #El método split(), aplicado a un string, crea una lista en la que cada elemento es una palabra del string.
    cypher_message = [] # Se crea una lista vacia con la variable cypher_message 

    for word in words: # recorre cada palabra en el mensaje ingresado
        cypher_word = '' #Se crea una variable con un string vacio
        for letter in word: # recorre cada letra en cada palabra
            cypher_word += KEYS[letter] # Lo que va a ser es construir cada letra y lo va a reemplazar por el mensaje cifrado

        cypher_message.append(cypher_word)# esta funcion lo que hace es indicar que cada letra se añada a la variable cypher_message que en incio es una lista vacia

    return ' '.join(cypher_message) # y el metodo join reemplaza cada espacio vacio en una letra de cypher message


def decipher(message): ## Descifrar -- se recibe el mensaje cifrado que se arroja en un inicio en el mismo codigo o de alguien que tenga la misma codificacion
    words = message.split(' ') # nuevamente se hace la funcion para separar letra por letra
    decypher_message = []# Se crea una lista vacia con la variable decypher_message

    for word in words:# recorre cada palabra en el mensaje ingresado
        decypher_word = '' #Se crea una variable con un string vacio
        for letter in word: # recorre cada letra en cada palabra
            for key, value in KEYS.items(): #no se puede acceder directamente al diccionario a traves de su valor, se itera a lo largo de las llaves y si se encuentra el valor, se puede obtener la llave
                if value == letter: # si el valor es igual a la letra despues de recorrer en las llaves significa que se encontro
                    decypher_word += key #almacene en la variable vacia, la llave

        decypher_message.append(decypher_word)# esta funcion lo que hace es indicar que cada letra se añada a la variable decypher_message que en incio es una lista vacia

    return ' '.join(decypher_message)# y el metodo join reemplaza cada espacio vacio en una letra de decypher_message
    


def run():

    while True:

        command = str(input( """ ---* ---* ---* ---* ---* ---* 
        
            Bienvenido a criptografia. ¿Que deseas hacer?

            [c]ifrar mensaje
            [d]escifrar mensaje
            [s]salir 
        
        """))

        if command == 'c':
            message = input('escribe tu mensaje: ') # message es el parametro que recipe la funcion cypher
            cypher_message = cypher(message)# la variable recibe la funcion con el paramatro al de cifrar
            print(cypher_message)# se imprime como tal lo que retorna la funcion cypher(message)
        elif command == 'd':
            message = input('Escribe tu mensaje cifrado: ')
            decypher_message = decipher(message)# la variable recibe la funcion con el paramatro al de descifrar
            print(decypher_message)# se imprime el mensaje descifrado
        elif  command == 's':
            sys.exit() # Pasa salir de forma correcta se debe importar la libreria sys en el inicio

        else:
            print('comando no encontrado')


if __name__ == "__main__":
    print('M E N S A J E S C I F R A D O S')
    run()
        



countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = input('Escribe el nombre de un pais: ').lower()

    try:
        print(f'La poblacion de {country} es: {countries[country]} millones')

    except KeyError:
        print(f'No tenemos el dato de la poblacion de {country}')
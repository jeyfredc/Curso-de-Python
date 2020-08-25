def recursive_sum(number):
    if number == 1:
        return 1
    else:
        suma = number
        suma += recursive_sum(number - 1)
        return suma


def run():
    while True:
        number = int(input('Escribe un número para sumar recursivamente: '))
        if number < 1:
            print('Nope.')
        else:
            result = recursive_sum(number)
        
        print(f'El resultado es: {result}')

global 


if __name__ == "__main__":
    run()
def binary_search(numbers, number_to_find, low, high):

    if low > high: # si el numero bajo es mayor que el alto retorna falso
        return False


    mid = (low+high)/2 #el numero bajo + el numero alto entre 2 es el numero medio 
    mid = int(mid)  

    if numbers[mid] == number_to_find: # si el numero de la mitad es igual al numero buscado
        return True
    elif numbers[mid] > number_to_find: # si el numero de la mitad es mayor que el numero buscado debo buscar un indice menor
        return binary_search(numbers, number_to_find, low, mid-1)
    else: # si el numero de la mitad es menor que el numero buscado debo buscar un indice mayor
        return binary_search(numbers, number_to_find, mid+1, high)



if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

    if result is True:
        print('El numero si esta en la lista')
    else:
        print('el numero no esta en la lista')

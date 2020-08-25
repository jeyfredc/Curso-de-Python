def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

""" Tener en cuenta que la forma de abrir y crear un archivo asi no exista es con el metodo write.

    Si no se utilizara el manejador de contexto with lo que se tendria que hacer a continuacion es esto:

try:
    f = open()
finally:
    f = close()

 """


if __name__ == "__main__":
    run()
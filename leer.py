def run():
    counter=0    
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')

    print(f'Beatriz se encuentra {counter} veces, en el texto')



if __name__ == "__main__":
    run()
def main():

    exp = 0
    result = 0

    nr = int(input("Digite um número binário: "))
    
    while nr != 0:
        cont = nr % 10
        nr = nr // 10

        x = cont * (2 ** exp)
        result = result + x
        exp += 1
    
    print(result)

main()

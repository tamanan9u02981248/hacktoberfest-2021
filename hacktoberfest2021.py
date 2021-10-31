import random

escolha = 1

def inverter_string():
    string = str(input("Digite a string para inverter: "))
    string = string[::-1].upper()
    print("resultado: {} \n".format(string))

def string_escada():
    string = str(input("Digite a string para exibir em cada: "))
    for index in range(len(string)+1):
        print(" ".join(list(string[0:index].upper())))
    print('\n')

def string_embaralhada():
    string = list(str(input("Digite a string para embaralhar: ")))
    random.shuffle(string)
    print("".join(string))

def menu():
    global escolha
    escolha = int(input("1 - Inverter String \n2 - String em Escada \n3 - Embaralhar string \n0 - sair \n\n"))

    if (escolha == 1):
        inverter_string()
    elif (escolha == 2):
        string_escada()
    elif (escolha == 3):
        string_embaralhada()

while (escolha != 0):
    menu()

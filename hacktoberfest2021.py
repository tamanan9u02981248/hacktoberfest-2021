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

def funcao_f(valor):
    if (valor == 1):
        return 1
    elif (valor == 0):
        return 0
    else:
        return funcao_f(valor - 1) + funcao_f(valor - 2)    

def calcular_fibonacci():
    n = int(input("Digite um número para calcular o valor de fibonacci: "))
    print("o resultado é {}".format(funcao_f(n)))

def menu():
    global escolha
    escolha = int(input("1 - Inverter String \n2 - String em Escada \n3 - Embaralhar string \n4 - Fibonacci \n0 - sair \n\n"))

    if (escolha == 1):
        inverter_string()
    elif (escolha == 2):
        string_escada()
    elif (escolha == 3):
        string_embaralhada()
    elif (escolha == 4):
        calcular_fibonacci()    

while (escolha != 0):
    menu()

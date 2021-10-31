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

def menu():
    global escolha
    escolha = int(input("1 - Inverter String \n2 - String em Escada \n0 - sair \n\n"))
    if (escolha == 1):
        inverter_string()
    elif (escolha == 2):
        string_escada()

while (escolha != 0):
    menu()

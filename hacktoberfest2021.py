escolha = 1

def inverter_string():
    string = str(input("Digite a string para inverter: "))
    string = string[::-1].upper()
    print("resultado: {} \n".format(string))

def menu():
    global escolha
    escolha = int(input("1 - Inverter String \n0 - sair \n\n"))
    if (escolha == 1):
        inverter_string()

while (escolha != 0):
    menu()

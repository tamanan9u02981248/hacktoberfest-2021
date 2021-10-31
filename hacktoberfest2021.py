escolha = 1

def menu():
    global escolha
    escolha = int(input("0 - sair \n\n"))

while (escolha != 0):
    menu()

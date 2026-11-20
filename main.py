ver_saldo = 1
depositar = 2
sacar = 3  
simular_rendimento = 4
sair = 0
i = -1
#Pede o nome do usuário e define um saldo inicial (ex: 1000.0)
print("Bem-vindo ao Caixa Eletrônico!")
nome = input("Digite seu nome: ")
saldo = float(input("Digite seu saldo inicial: "))

#Mostra um menu dentro de um while:
while i != 0:
    print("\nEscolha uma opção:")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Simular rendimento")
    print("0 - Sair")
    i = int(input())
    if i == 1:
        print(f"Seu saldo atual e de R${saldo}")
    if i == 2:
        deposito = float(input("Deseja depositar quanto?"))
        saldo = deposito + saldo
        print(f"Seu saldo atual e de R${saldo}")
    if i == 3:
        saque = float(input("Deseja sacar quanto?"))
        if saque > saldo:
            print("Saldo insuficiente")
        else:
            saldo = saldo - saque
            print(f"Seu saldo atual e de R${saldo}")
    if i == 4:
        rendimento = float(input("Deseja simular com qual taxa?"))
        valor_para_render = float(input("Deseja simular com qual valor?"))
        meses = float(input("Deseja simular com quantos meses?"))
        valor_rendido = (rendimento/100) * valor_para_render * meses
        valor_final = valor_rendido + valor_para_render
        print(f"\nNo periodo rendeu R${valor_rendido}")
        print(f"\nAo final voce tera R${valor_final}")
    if i == 0:
        print("voce saiu")
        break


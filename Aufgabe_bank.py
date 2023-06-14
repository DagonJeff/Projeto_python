import Class_bank
#----------------------------EXECUÇÂO-----------------------------#


bank = Class_bank.Bank()

#Cadastro de contas
while bank.noch < 10:
    neue_konto = int(input("--------------------\nNúmero da conta:"))
    
    konto_saldo = float(input("Saldo R$:"))
    bank.konto_erstellen(neue_konto, konto_saldo)    

#Relizando operações nas contas

while True:
    
    wahl = int(input("|---------Escolha uma opção---------|\n1. Realizar Depósito\n2. Realizar Saque\n3. Consultar o ativo bancário\n4. Consultar todas contas\n5. Finalizar Programa\n"))
    
    if wahl == 5:
        break
    
    elif wahl == 1:
        
        konto = int(input("--------------------\nNúmero da conta:"))
        #Chamando o método que verifica se a conta existe
        idx  = bank.konto_suche(konto)
        #Se exitir irá retornar o valor do índice dela na lista
        if type(idx) == int:
            betrag = float(input("Valor do deposito R$:"))
            bank.konto_einzahlen(idx, betrag)
            
        else:
            print(idx)
        
    elif wahl == 2:
        
        konto = int(input("--------------------\nNúmero da conta:"))
        #Chamando o método que verifica se a conta existe
        idx = bank.konto_suche(konto)
        #Se exitir irá retornar o valor do índice dela na lista
        if type(idx) == int:
            betrag = float(input("Valor do Saque R$:"))
            bank.konto_abheben(idx, betrag)
            
        else:
            print(idx)
    
    elif wahl == 3:
        #Chamando o método de somatória das contas já possui de retorno a função print()
        bank.total_salden()
    
    elif wahl == 4:
        #Chamando o método de consulta de todas as contas
        bank.druck_konten()
        
    else:
        print("Digite uma opção válida!")
        

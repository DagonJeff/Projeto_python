class Bank:
        
    def __init__(self):
        self.konten = [] #lista de núemros das contas
        self.salden = [] #lista dos saldos
        self.noch = 0
        pass
           
        
    #Criando conta e salvando saldo na lista de saldos no mesmo indice da conta
    def konto_erstellen(self, konto, saldo):

        ver = Bank.konto_suche(self, konto)
        
        if type(ver) == int:
            print("Conta já existe")

        else:
            self.konten.append(konto)
            ind = self.konten.index(konto)
            self.salden.insert(ind, saldo)
            self.noch += 1
                             
    #método de consulta de todas as contas e seus respectivos saldos
    def druck_konten(self):
        
        for konto, saldo in zip(self.konten, self.salden):
            print('--------------------\nConta:{}\nSaldo R${: .2f}'.format(konto, saldo))
        print("--------------------")

    #método de somatótio do saldo de todas as contas
    def total_salden(self):
        total = 0.0
        for y in self.salden:
            total += y
        print(f'Saldo Total R$:{total: .2f}\n-------------------------')
    
    #método de verificação de existência de conta
    def konto_suche(self, konto):
        
        ind = "Nenhuma conta cadastrada"
        for x in self.konten:
            if x == konto:
        #Capturando o indíce da conta quando já existente
                ind = self.konten.index(konto)
                return ind
                
            else:
                ind = "Conta não encontrada!"
                
        return ind

    #método de depósito
    def konto_einzahlen(self, ind, saldo):
        
        self.salden[ind] += saldo
    
    #método de saque
    def konto_abheben(self, ind, saldo):
        
        if saldo <= self.salden[ind]:
         self.salden[ind] -= saldo
        else:
            print("Saldo insuficiente!")
       
    
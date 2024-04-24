from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereço = endereco
        self.contas = []
        
    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome,data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        

class Conta:
    def __init__(self, numero, Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = Cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia 
    
    @property
    def cliente(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        execedeu_saldo = valor > saldo
        
        if execedeu_saldo:
            print("\n@@@Operação Falhou! Você não tem saldo suficiente. @@@")
            
        elif valor > 0:
            self._saldo -=valor
            print("\n@@@Saque realizado com sucesso!@@@")
            return True
        else:
            print("\n@@@ Operação falhou! Ovalor informado é invalido.@@@")
            
        return False
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n@@@ Deposito realizado com sucesso! @@@")
            
        else:
            print("\n@@@ Operação falhou! Ovalor informado é invalido.@@@")
            
        return True

class Historico:
    def __init__(self):
    self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
            "tipo": transacao.__class__.__name__
            "valor":transacao, valor,
            "data": detetime.now().strftime
            ("%d-%m-%y  %H:%M:%s"),
            }
        )
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self)
        pass
        
    @abstractclassmethod
    def registrar(self,conta):
        pass
        
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
        @property
        def valor(self)
            return self._valor
            
        def registrar(self, conta):
            sucesso_transacao = conta.sacar(self.valor)
            
            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)
                
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
        @property
        def valor(self):
            return self._valor
            
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)
            
            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
     def sacar(self, valor):
        
        numero_saques = len(
    [transacao for transacao in self.historico.transacoes if transacao['tipo']== Saque.__name__]
        

    excedeu_limite = valor > self.limite
    execedeu_saques = numero_saques >= self.limite_saques
    
     if excedeu_limite:
        print("\n@@@Operação Falhou! O valor do Saque excedeu o limite. @@@")
        
    elif execedeu_saques:
        print("\n@@@Operação Falhou! Você excedeu o numero de saques diarios. @@@")
        
    else:
         return super()sacar(valor)
    
    return False
    
    def __str__(self):
        return f"""\
            agencia:\t{self.agencia}
            c/c:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """
    return True
    


#parte dois do desafio
def menu():
    menu = """\n
    ============== MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def main():
    Cliente = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            Depositar(Cliente)
            
        elif opcao == "s":
            Sacar(Cliente)
            
        elif opcao == "e":
            Exibir_extrato(Cliente)
            
        elif opcao == "nu":
            criar_clientes(Cliente)  
            
        elif opcao == "nc" :
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, Cliente, contas)
            
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("\n@@@ Operação invalida, por favor selecionenovamente a operação desejada.@@@")
    
def filtrar_clientes(cpf. clientes):
    clientes_filtrados = [cliente for cliente in
    clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados
    else None
    
def recuperar_conta_clientes(cliente):
    if not cliente.contas:
        print("\n @@@Cliente não possui conta! @@@")
        return
       FIXME:
    return cliente.contas[0]
    
def sacar(clientes):
    cpf = input("Informe o cpf do cliente: ")
    Cliente = filtrar_clientes(cpf, clientes)
    
    if not Cliente:
        print("\n @@@Clientes não encontrado! @@@")
        return 
    valor = float(input("Informeo valor do saque: "))
    Transacao = Saque(valor)
    
    conta = recuperar_conta_clientes(Cliente)
    if not conta:
        return
        
def exibir_extrato(clientes):
    cpf = input("Informe o cpfdo cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("\n @@@ Cliente não encontrado!@@@ ")
        return
    Conta = recuperar_conta_clientes(cliente)
    if not Conta:
        return
    
    print("\n===================Extrato ===============")
    Transacoes = conta.historico.transacoes
    
    extrato = ""
    if not Transacoes:
        extrato = "não foram realizadas movimentações."
    else:
        for transacao in Transacoes:
            extrato += f"\n{Transacao['tipo']}:\n\tR$
            {transacao['valor']:.2f}"
            
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("============================================")
    
def criar_clientes(clientes):
    cpf = input("Informe o CPF (somente números): ") 
    Cliente = filtrar_clientes(cpf, clientes)
    
    if Cliente:
        print("\n@@@ já existe clientes com esse cpf:   @@@@")
        return
    
    nome = input("infomre o nome completo! ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (rua - bairod - cidade- Estado/silga): ")
    
    Cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf,endereco=endereco)
    
    clientes.append(Cliente)
    print("\n@@@ Cliente criado com sucesso!  @@@@") 
     
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    Cliente = filtrar_clientes(cpf, clientes)
    
    if not Cliente:
        print("\n@@@Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    conta = ContaCorrente.nova_conta(Cliente=Cliente,
    numeor=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n@@@ Conta criada com sucesso! @@@")
    
def listar_contas(contas):
    for conta in contas:
        print("=" = 100)
        print(textwrap.dedent(str(conta)))
      
def depositar(clientes):
    cpf = input("Informe o cpfdo cliente: ")
    Cliente = filtrar_cliente(cpf, clientes)
    
    if not Cliente:
        print("\n@@@ Cliente não encontrado!  @@@")
        return
    valor = float(imput("Informe o valor do deposito": ))
    
    Transacao = Deposito(valor)
    
    Conta = recuperar_conta_cliente(clientes)
    if not Conta
    return

    clientes.realizar_transacao(Conta, Transacao)
          
    
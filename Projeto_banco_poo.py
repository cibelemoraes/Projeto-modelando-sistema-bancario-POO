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
    


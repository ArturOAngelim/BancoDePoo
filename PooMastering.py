
class ContaBancaria:
    def __init__(self,saldo,nome,data):
        self.saldo=saldo
        self.nome=nome
        self.idade=data
    def nascimento(self):
        return 2026-self.data

class Poupanca(ContaBancaria):
    def __init__(self,nome,guardar_dinheiro,caixinha,saldo,idade):
        super().__init__(saldo,nome,idade)
        self.guardar_dinheiro=guardar_dinheiro
        self.caixinha=caixinha

    def depositar(self,saldo):
        super().__init__(saldo)
        conta=[]
        if saldo>=1:
            conta.append(saldo)

    def retirar(self,saldo,retirada):
        super().__init__(saldo)
        if retirada>=self.saldo:
            self.saldo-=retirada
        else:
            print(f"Saldo insulficinte")
class caixinha:
    def __init__(self,saldo):
       self.saldo=saldo 
    def rendimento(self,saldo):
        if self.saldo>=1:
            tr=0.0017
            rendimento_mensal=0.005+tr
            rendimento=self.saldo*rendimento_mensal

            self.saldo+=rendimento

            return rendimento
        return 0

    def retirada_caixinha(self,saldo,ret_caixinha):
        if self.saldo>=ret_caixinha:
            self.saldo-=ret_caixinha
        else:
            print(f"Saldo Insulficiente")

class Corrente(ContaBancaria):
    def __init__(self, nome, saldo, idade, limite):
            super().__init__(saldo, nome, idade)

            self.limite = limite
            self.historico = []

            self.pix = self.Pix(self)
            self.debito = self.Debito(self)
            self.credito = self.Credito(self, limite)

    def depositar(self,valor):
        if valor>=0:
            self.saldo+=valor
            self.historico.append(f"Deposito de +{valor:.2f}")

    def pagar(self,saldo):
        if self.saldo>=saldo:
            self.saldo-=saldo
            self.historico.append(f"Pago com o valor de {saldo:.2f}")
        else:
            print("Ocorreu um erro durante a transação!")

    def sacar(self,valor):
        if valor<=0:
            print("Valor invalido")
            return
        if valor<=self.saldo+self.limite:
            self.saldo-=valor
            self.historico.append(f"retirada de -{valor:.2f}")
        else:
            print(f"Valor insulficiente para retirada   ")

    def trasnferencia(self,saldo,conta_destino):
        if saldo<=self.saldo+self.limite:
            self.saldo-=saldo
            conta_destino.saldo+=saldo
            self.historico.append(f"Transferencia de R${saldo:.2f} Realizada com sucesso")

            conta_destino.historico.append(f" tranferencia de R${saldo:.2f} recebida com sucesso")
        else:
            print("Ocorreu um erro durante a transação!")

    def consultar(self):
        return self.saldo

    def consultar_historico(self):
        for transacao in self.historico:
            print(transacao)
    class Pix():
        def __init__(self,conta):
            self.conta=conta
            self.historico=[]
            self.chaves=[]
        def cadastrar_chave(self,chave):
            if chave not in self.chaves:
                self.chaves.append(chave)
                print(f"Chave {chave} cadastrada com sucesso")
            else:
                print(f"Chave ja cadastrada")
        def remover_chave(self,chave):
            if chave in self.chaves:
                self.chaves.remove(chave)
                print(f"Chave removida com sucesso")
            else:
                print(f"Chave não cadastrada")
        def consultar_chaves(self):
            return self.chaves
        def enviar(self,valor,conta_destino):
            if valor<=0:
                print("Erro")
                return
            if self.conta.saldo>=valor:
                self.conta.saldo-=valor
                conta_destino.saldo+=valor

                self.historico.append(f"PIX enviado: -R${valor:.2f}"
                )

                print(
                    f"PIX de R${valor:.2f} enviado com sucesso!"
                )
            else:
                print("Saldo insuficiente.")
        def receber(self,valor):
            if valor> 0:
                self.conta.saldo+=valor
                self.historico.append(f"PIX recebido: +R${valor:.2f}"
                )

                print(
                    f"PIX de R${valor:.2f} recebido com sucesso!"
                )
        def consultar_historico(self):
            print("Historico do PIX:")
            for transacao in self.historico:
                print(transacao)

    class Debito():
        def __init__(self,conta):
            self.conta=conta
            self.bloqueado=False
            self.senha="123456"
            self.historico=[]
        def comprar(self,valor):
            if self.bloqueado:
                print("Cartao Bloqueado")
                return
            if self.conta.saldo>=valor:
                self.conta.saldo-=valor
                self.historico.append(f"Compra de {valor} concluida com sucesso")
                print("Compra Aprovada")
            else:
                print("Saldo insulficiente")
        def consultar_saldo(self):
            return(self.conta.saldo)
        def bloquear(self):
            self.bloqueado=True
        def desbloquear(self):
            self.bloqueado=False
        def alterar_senha(self,nova_senha):
            if self.senha == nova_senha:
                print("Não é possível usar a mesma senha.")
            else:
                self.senha = nova_senha
                print("Senha alterada com sucesso!")
        def consultar_limite(self):
            return self.conta.saldo
        def consultar_historico(self):
            return self.historico
        def estornar(self,valor):
            self.conta.saldo+=valor
            self.historico.append({
            "tipo": "estorno",
            "valor": valor
        })
            print(f"Estorno de R${valor:.2f} realizado!")
    class Credito():
        def __init__(self,conta,limite):
            self.conta=conta
            self.limite=limite
            self.fatura=0
            self.bloqueado=False
            self.historico=[]
            self.senha="123456"
            self.compras=[]
            self.proximo_id=0
        def comprar(self,valor):
            if self.bloqueado is True:
                print("Cartão Bloqueado")
                return

            if valor <= self.limite - self.fatura:

                compra = {
                    "id": self.proximo_id,
                    "valor": valor,
                    "cancelada": False
                }

                self.compras.append(compra)
                self.proximo_id += 1
                self.fatura += valor

                print(f"Compra #{compra['id']} realizada!")
            else:
                print("Limite insuficiente.")


        def consultar_fatura(self):
            return self.fatura
        def consultar_limite(self):
            return self.limite-self.fatura
        def pagar_fatura(self):
            if self.conta.saldo>=self.fatura:
                self.conta.saldo-=self.fatura
                self.fatura=0
                print("Fatura paga!")
            else:
                print("Saldo insuficiente para pagar a fatura.")
        def aumentar_limite(self,valor):
            if valor>0:
                self.limite+=valor
                print(f"Limite aumentado para R${self.limite:.2f}")
            else:
                print("Valor inválido.")
        def bloquead(self):
            if self.bloqueado is False:
                self.bloqueado=True
        def desbloqueado(self):
            if self.bloqueado is True:
                self.bloqueado=False
        def alterar_senha(self,nova_senha):
            if self.senha==nova_senha:
                print("Esta senha esta em uso")
            if self.senha!=nova_senha:
                self.senha=nova_senha
        def consultar_historico(self):
            return self.historico
        def estornar(self, valor):
            if valor <= self.fatura:
                self.fatura -= valor
                self.historico.append(
                    f"Estorno de R${valor:.2f}"
                )
                print(f"Estorno de R${valor:.2f} realizado!")
            else:
                print("Valor do estorno é maior que a fatura.")
        def cancelar_compra(self,id_compra):
            for compra in self.compras:

                if compra["id"] == id_compra:

                    if compra["cancelada"]:
                        print("Essa compra já foi cancelada.")
                        return

                    compra["cancelada"] = True
                    self.fatura -= compra["valor"]

                    print(
                        f"Compra #{id_compra} cancelada!"
                    )

                    return

            print("Compra não encontrada.")


print("=" * 50)
print("TESTE DO SISTEMA BANCÁRIO")
print("=" * 50)


# ==========================================
# CRIANDO AS CONTAS
# ==========================================

joao = Corrente(
    nome="João",
    saldo=1000,
    idade=25,
    limite=500
)

maria = Corrente(
    nome="Maria",
    saldo=500,
    idade=30,
    limite=300
)

print("\nCONTAS CRIADAS")

print(f"João: R${joao.saldo:.2f}")
print(f"Maria: R${maria.saldo:.2f}")


# ==========================================
# DEPÓSITO
# ==========================================

print("\n--- DEPÓSITO ---")

joao.depositar(500)

print(f"Saldo João: R${joao.saldo:.2f}")


# ==========================================
# SAQUE
# ==========================================

print("\n--- SAQUE ---")

joao.sacar(200)

print(f"Saldo João: R${joao.saldo:.2f}")


# ==========================================
# TRANSFERÊNCIA
# ==========================================

print("\n--- TRANSFERÊNCIA ---")

joao.trasnferencia(300, maria)

print(f"Saldo João: R${joao.saldo:.2f}")
print(f"Saldo Maria: R${maria.saldo:.2f}")


# ==========================================
# PIX
# ==========================================

print("\n--- PIX ---")

joao.pix.cadastrar_chave("joao@email.com")

print("Chaves João:")
print(joao.pix.consultar_chaves())

joao.pix.enviar(100, maria)

print(f"Saldo João: R${joao.saldo:.2f}")
print(f"Saldo Maria: R${maria.saldo:.2f}")


# ==========================================
# PIX RECEBIMENTO
# ==========================================

print("\n--- PIX RECEBIDO ---")

maria.pix.receber(200)

print(f"Saldo Maria: R${maria.saldo:.2f}")


# ==========================================
# CARTÃO DE DÉBITO
# ==========================================

print("\n--- CARTÃO DE DÉBITO ---")

joao.debito.comprar(100)

print(f"Saldo João: R${joao.saldo:.2f}")

print("Saldo disponível no débito:")
print(joao.debito.consultar_saldo())


# ==========================================
# ESTORNO DO DÉBITO
# ==========================================

print("\n--- ESTORNO DÉBITO ---")

joao.debito.estornar(100)

print(f"Saldo João: R${joao.saldo:.2f}")


# ==========================================
# BLOQUEIO DO DÉBITO
# ==========================================

print("\n--- BLOQUEIO DÉBITO ---")

joao.debito.bloquear()

joao.debito.comprar(50)

joao.debito.desbloquear()

joao.debito.comprar(50)

print(f"Saldo João: R${joao.saldo:.2f}")


# ==========================================
# CARTÃO DE CRÉDITO
# ==========================================

print("\n--- CARTÃO DE CRÉDITO ---")

print(
    f"Limite inicial: "
    f"R${joao.credito.consultar_limite():.2f}"
)

joao.credito.comprar(500)

print(
    f"Fatura: "
    f"R${joao.credito.consultar_fatura():.2f}"
)

print(
    f"Limite disponível: "
    f"R${joao.credito.consultar_limite():.2f}"
)


# ==========================================
# SEGUNDA COMPRA NO CRÉDITO
# ==========================================

print("\n--- SEGUNDA COMPRA CRÉDITO ---")

joao.credito.comprar(200)

print(
    f"Fatura: "
    f"R${joao.credito.consultar_fatura():.2f}"
)

print(
    f"Limite disponível: "
    f"R${joao.credito.consultar_limite():.2f}"
)


# ==========================================
# CANCELAMENTO DE COMPRA
# ==========================================

print("\n--- CANCELAMENTO ---")

joao.credito.cancelar_compra(0)

print(
    f"Fatura depois do cancelamento: "
    f"R${joao.credito.consultar_fatura():.2f}"
)


# ==========================================
# AUMENTAR LIMITE
# ==========================================

print("\n--- AUMENTAR LIMITE ---")

joao.credito.aumentar_limite(1000)

print(
    f"Limite total: "
    f"R${joao.credito.limite:.2f}"
)

print(
    f"Limite disponível: "
    f"R${joao.credito.consultar_limite():.2f}"
)


# ==========================================
# PAGAMENTO DA FATURA
# ==========================================

print("\n--- PAGAMENTO DA FATURA ---")

print(f"Saldo antes: R${joao.saldo:.2f}")

joao.credito.pagar_fatura()

print(f"Saldo depois: R${joao.saldo:.2f}")

print(
    f"Fatura atual: "
    f"R${joao.credito.consultar_fatura():.2f}"
)


# ==========================================
# HISTÓRICO
# ==========================================

print("\n--- HISTÓRICO DA CONTA ---")

joao.consultar_historico()

print("\n--- HISTÓRICO PIX ---")

joao.pix.consultar_historico()

print("\n--- HISTÓRICO DÉBITO ---")

print(joao.debito.consultar_historico())

print("\n--- HISTÓRICO CRÉDITO ---")

print(joao.credito.consultar_historico())
from Venda import Venda
from ProdutoEstoque import ProdutoEstoque
from ProdutoVenda import ProdutoVenda
class Caixa (Venda, ProdutoEstoque, ProdutoVenda) :
    def __init__(self) :
        self.__produtos = {}
        self.__vendas = []
        
    @classmethod
    def menu (cls):
        print()
        print('***********************************')
        print('*            CAIXA                *')
        print('***********************************')
        print('(C) Cadasta/atualizar')
        print('(E) Entrada de estoque')
        print('(V) Vender')
        print('(R) Relatorio de vendas')
        print('(S) Sair')
        print('***********************************')
        escolha = input('Informe a operação: ').upper()
        return escolha
    
    def busca_produto(self):
        if len(self.__produtos) == 0:
            print('Nenhum produto cadastrado!')
            return None
        print('\nProdutos:')
        for cod,produto in self.__produtos.items():
            print(cod, ':' ,produto)
        codigo = Venda.pergunta('Codigo do produto: ')
        if codigo in self.__produtos:
            return self.__produtos[codigo]
        print('Produto não encontrado !')
        return None

    @classmethod
    def dados_produtos(cls):
        print('\n Informe os dados')
        descricao = input('Descricao: ')
        preco = Venda.pergunta('Preco: ',float)
        return descricao,preco
    
    def cadastro_produto (self):
        produto = self.busca_produto()
        if produto is  None:
            print('Produto cadastrado: ', produto)
            if Venda.confirma('Alterar?(S/N)','S'):
                descricao,preco = self.dados_produtos()
                produto.descricao = descricao
                produto.preco = preco
            else:
                if Venda.confirma('Incluir?(S/N', 'S'):
                    descricao,preco = self.dados_produtos()
                    produto = ProdutoEstoque(descricao,preco)
                    codigo = len(self.__produtos)
                    self.__produtos[codigo] = produto
    
    def entrada_estoque(self):
        produto = self.busca_produto()
        if produto is not None:
            quantidade = Venda.pergunta('Quantidade de entrada: ' , float)
            produto.entrada(quantidade)
    
    def venda(self):
        print("Venda")
        venda = Venda()
        produtoVenda = ProdutoVenda()
        while True:
            produto = self.busca_produto()
            if produto is not None:
                quantidade  = venda.pergunta("Quanditade vendida:", float)
                if produto.saida(quantidade):
                    produto_venda = ProdutoVenda(produtoVenda.__descriacao,
                                                 produtoVenda.__preco,
                                                 quantidade)
                    venda.adicionar_produto(produto_venda)
            print(venda)
            if Venda.confirma('Adicionar mais produtos? (S/N)'):
                break
            if Venda.numero_produtos>0:
                self.__vendas.append(venda)
            
    def relatorio_vendas(self):
        if len(self.__vendas) == 0:
             print('Nenhum vendas encontrada')
             return 
        total_geral = 0
        for cont,venda in enumerate (self.__vendas):
            print('\nVenda'. cont)
            print(venda)
            total_geral += Venda.total
            print('TOTAL GERAL: ' , total_geral)
            input ('Presione ENTER para voltar')
    
    def iniciar(self):
        while True:
            escolha = self.menu()
            if escolha == 'C':
                self.cadastro_produto()
            elif escolha == 'E':
                self.entrada_estoque()
            elif escolha == 'V':
                self.venda()
            elif escolha == 'R':
                self.relatorio_vendas()
            elif escolha == 'S':
                break
            

                
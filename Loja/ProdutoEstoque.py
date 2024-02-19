from Produto import Produto

class ProdutoEstoque(Produto):
    def __init__(self, descricao,preco) :
        super().__init__(descricao,preco)
        self.__estoque = 0.0
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco
    
    @property
    def descricao(self):
        return self.__descriacao

    @descricao.setter
    def descricao(self,descricao):
        self.__descriacao = descricao
    
    def entrada_estoque(self,quantidade):
        self.__estoque += quantidade
        
    def saida_estoque(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
            return True
        return False
    
    def __str__(self):
        texto = super ().__str__()
        texto += ', Estoque : {e:0.3f}'.format(e=self.__estoque)
        
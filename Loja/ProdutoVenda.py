from Produto import Produto

class ProdutoVenda(Produto):
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self.__quantidade = quantidade
    
    @property
    def total_estoque(self):
        return self.__quantidade * self.__preco
    
    def __str__(self):
        texto = super().__str__()
        texto+= ', Qtde: {q:0.3f}'.format(q=self.__quantidade)
        texto+= ', Total: ${t:0.2f}'.format(t = self.total)
        
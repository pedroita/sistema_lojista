class Produto:
    def __init__(self,descricao,preco) :
        self.__descriacao = descricao
        self.__preco = preco
        
    def __str__(self) :
        return '{d}(${p:0.2f})'.format(
            d=self.__descriacao,
            p=self.__preco
        )
    
        
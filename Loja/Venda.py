
class Venda:
    def __init__(self) :
        self.__produtos = []
        self.__total = 0
    
    @property
    def total (self):
        return self.__total
    @property
    def numero_produtos(self):
        return len(self.__produtos)
    
    def adicionar_produto(self,produto):
        self.__produtos.append(produto)
        self.__total += produto.total
    
    def __str__(self) :
        texto = '\n' + '-'*50
        texto += '\nProdutos:'
        for produto in self.__produtos:
            texto += '\n' + str(produto)
        texto += '\n' +'-'*50
        texto += 'Total da venda: ${t:0.2f}'.format(t=self.__total)
        texto += '\n' + '-'*50
        return texto
    
    def pergunta(mesagem, tipo= int ):
        while True:
            try:
                resp = input (mesagem)
                return tipo(resp)
            except:
                print('Valor inválido! Informe novamente.')
    
    def confirma(mesagem,resposta):
        texto = input(mesagem).strip()
        if texto.lower() == resposta.lower():
            return True
        return False
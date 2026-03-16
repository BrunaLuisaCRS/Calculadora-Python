class Calculadora():
    def __init__(self):
        self.expressao = ""

    ''' determina o corpo da calculadora, onde a expressão é o que o usuário digita e o resultado é o que a calculadora retorna'''

    def adicionar(self, valor):
        self.expressao += str(valor)
        return self.expressao
    
    ''' adiciona algum valor à expressão, convertendo-o para string e concatenando-o com a expressão existente. Retorna a expressão atualizada.'''
    
    def limpar(self):
        self.expressao = ""
        return self.expressao
    
    ''' limpa a expressão, definindo-a como uma string vazia. Retorna a expressão limpa.'''

    def calcular(self):

        try:
            resultado = str(eval(self.expressao))
            self.expressao = resultado
            return resultado
        except:
            self.expressao = ""
            return "Erro"

        '''calcula o resultado da expressão usando a função eval() (que calcula automaticamente uma string de valores) e retorna o resultado. Se houver um erro na expressão, retorna "Erro".'''
     
        ''' self.expressao = "" retorna 'erro' e limpa a expressão para evitar que o usuário continue a usar uma expressão inválida. Isso é importante para garantir que a calculadora funcione corretamente e não retorne resultados incorretos ou cause erros adicionais. "" é equivalente a qulquer função invalida, como dividir por zero ou usar caracteres não numéricos. '''

        '''O uso de eval() pode ser perigoso se a entrada do usuário não for controlada, pois pode executar código malicioso. Em um ambiente de produção, é recomendável usar uma biblioteca de análise de expressões matemáticas segura em vez de eval(). Aqui, como tem fins de aprendizado, resolvi fazer 2 versões, uma usando eval() e outra usando parseamento manual para evitar os riscos associados ao eval().'''

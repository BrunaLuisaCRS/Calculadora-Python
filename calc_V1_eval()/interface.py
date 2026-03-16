import tkinter as tk 
''' importa a biblioteca de interface visual do Python'''
from calculadora import Calculadora
''' Imorta a classe 'Calculadora' da pasta 'calculadora' '''

class Interface:
    def __init__(self):

        self.calc = Calculadora() 
        ''' Cria uma instância da classe 'Calculadora' e a atribui à variável 'calc'. Isso permite que a interface interaja com a lógica da calculadora.'''

        self.janela = tk.Tk() 
        '''Cria a janela principal da interface usando a classe Tk() da biblioteca tk'''
        self.janela.title("Calculadora Eval") 
        '''Cria o título'''
        self.janela.geometry("300x400")
        ''' Define o tamanho da janela para 300 pixels de largura e 400 pixels de altura.'''
        self.janela.minsize(400, 400)
        self.display = tk.Entry(self.janela, font=("Arial", 20), justify="left")
        '''Cria um campo de entrada (Entry) para exibir os valores digitados e o resultado da operação. esse campo é adicionado à janela principal (self.janela) e tem uma fonte personalizada e alinhamento à esquerda.'''
        self.display.pack(fill="both", padx=10, pady=10)
        '''Adiciona o campo de entrada à janela usando o método pack(), que organiza os widgets na janela. O argumento fill="both" faz com que o campo de entrada se expanda para preencher todo o espaço disponível, enquanto padx=10 e pady=10 adicionam um preenchimento de 10 pixels ao redor do campo de entrada para melhorar a aparência.'''
        self.criar_botoes()

    def criar_botoes(self):
        botoes = [
            ('7','8','9','C','='),
            ('4','5','6','/','*'),
            ('1','2','3','-','+'),
            ('0','.'),
        ]
        '''Cria uma lista de tuplas, onde cada tupla representa uma linha de botões na calculadora. Cada elemento dentro da tupla é o rótulo do botão correspondente.'''
        for linha in botoes:
            linha_frame = tk.Frame(self.janela)
            '''Cria um frame para cada linha de botões. O frame é um contêiner que agrupa os botões em uma linha.'''
            linha_frame.pack()
            '''Adiciona o frame da linha à janela principal usando o método pack(). Isso organiza os frames verticalmente na janela.'''

            for botao in linha:
                b = tk.Button(linha_frame, text=botao,width=5, height=2, font=("Arial", 18), command=lambda x=botao: self.clique_botao(x))
                '''Cria um botão para cada rótulo na linha. O botão é adicionado ao frame da linha correspondente. O argumento command define a função a ser chamada quando o botão for clicado, passando o rótulo do botão como argumento.'''
                b.pack(side=tk.LEFT, padx=5, pady=5)
                '''Adiciona o botão ao frame da linha usando o método pack(), alinhando-o à esquerda (side=tk.LEFT) e adicionando um preenchimento de 5 pixels ao redor do botão para melhorar a aparência.'''
    def clique_botao(self, valor):
        if valor == 'C':
            texto = self.calc.limpar()
            self.atualizar_display(texto)
        elif valor == '=':
            texto = self.calc.calcular()
            self.atualizar_display(texto)
        else:
            texto = self.calc.adicionar(valor)
            self.atualizar_display(texto)
            '''Define a função clique_botao, que é chamada quando um botão é clicado. O valor do botão clicado é passado como argumento. A função verifica se o valor é 'C' (limpar), '=' (calcular) ou outro valor (adicionar à expressão) e chama os métodos correspondentes da classe Calculadora. Em seguida, atualiza o display com o resultado ou a expressão atualizada.'''

    def atualizar_display(self, texto):
        self.display.delete(0, tk.END)
        '''Limpa o conteúdo atual do campo de entrada (display) usando o método delete(). O argumento 0 indica o início do texto e tk.END indica o final do texto, garantindo que todo o conteúdo seja removido.'''
        self.display.insert(tk.END, texto)
        '''Insere o novo texto no campo de entrada usando o método insert(). O argumento tk.END indica a posição onde o texto deve ser inserido (final do campo), e texto é a string que será exibida no display.'''

    def iniciar(self):
        self.janela.mainloop()
        '''Inicia o loop principal da interface gráfica, permitindo que a janela seja exibida e interativa. O método mainloop() mantém a janela aberta e responde aos eventos do usuário, como cliques nos botões.'''




from interface import Interface
'''Importa a classe 'Interface' do módulo 'interface'.'''

def main():
    app = Interface()
    app.iniciar()
    '''Define a função main(), que é o ponto de entrada do programa. Dentro dessa função, uma instância da classe Interface é criada e o método iniciar() é chamado para iniciar a interface gráfica da calculadora.'''

if __name__ == "__main__":
    main()
    '''Verifica se o script está sendo executado diretamente (em vez de importado como um módulo) e, se for o caso, chama a função main() para iniciar o programa.'''
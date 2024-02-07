from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify

class Metodo():
    def __init__(self, f, a, b, erro, iters, g = 0):
        self.f = f
        self.a = a
        self.b = b
        self.erro = erro
        self.iters = iters
        self.g = g

    def get_a(self):
        return float(self.a)

    def set_a(self, a):
        self.a = a

    def get_b(self):
        return float(self.b)

    def set_b(self, b):
        self.b = b

    def get_erro(self):
        return float(self.erro)

    def get_iters(self):
        return int(self.iters)

class Bissecao(Metodo):
    def __init__(self, f, a, b, erro, iters):
        Metodo.__init__(self, f, a, b, erro, iters)

    def executa(self):
        print("\n* Solução *")

        for i in range(self.get_iters()):
            print(f"\nIteração {i}")
            # print(f"a = {self.get_a()}")
            # print(f"b = {self.get_b()}")

            # Calcula x
            x = (self.get_a() + self.get_b()) / 2
            print(f"x = {x}")

            # Calcula f(a) e f(b)
            fa = self.f(self.get_a())
            fb = self.f(self.get_b())
            # print(f"f(a) = {fa}")
            # print(f"f(b) = {fb}")

            # Calcula f(x)
            fx = self.f(x)
            print(f"f(x) = {fx}")

            # Verifica se encontrou a raíz
            if self.f(x) == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz x = {x} em {self.get_iters()} iterações.")
                return
            
            # Verifica o critério de erro tolerado
            if abs(self.f(x)) <= self.get_erro():
                print(f"\nAlgoritmo encerrado!")
                print(f"f(x) = {self.f(x)} já está próximo o suficiente.")
                print(f"Raíz aproximada encontrada em {i+1} iterações: x = {x}.")
                return

            else:
                # Verifica se f(x) tem o mesmo sinal de f(a) ou de f(b)
                if fx * fa > 0:
                    # print(f"f(x) tem o mesmo sinal de f(a)")
                    # Altera o a
                    self.set_a(x)
                else:
                    # print(f"f(x) tem o mesmo sinal de f(b)")
                    # Altera o b
                    self.set_b(x)

            input()

        # Iterações finalizadas
        print(f"\nAlgoritmo encerrado!")
        print(f"Valor encontrado em {i+1} iterações: {fx}.")
        return


class PontoFixo(Metodo):
    def __init__(self, f, g, a, b, erro, iters,):
        Metodo.__init__(self, f, a, b, erro, iters, g = g)

    def executa(self):

        print("\n* Solução *")

        # A aproximação inicial de X vai ser na metade do intervalo [a,b]
        x = (self.get_a() + self.get_b()) / 2

        for i in range(self.get_iters()):
            print(f"\nIteração {i}")
            print(f"a = {self.get_a()}")
            print(f"b = {self.get_b()}")

            # Verifica se g(x) é convergente
            # primeiro critério: o módulo da derivada é < 1 para todo x pertencente ao intervalo [a,b]
            # segundo critério: x0 está dentro do intervalo [a,b]

            print(f"x = {x}")

            # Calcula f(x)
            fx = self.f(x)
            print(f"f(x) = {fx}")

            # Verifica se encontrou a raíz
            if self.f(x) == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz x = {x} em {self.get_iters()} iterações.")
                return
            
            # Verifica o critério de erro tolerado
            if abs(self.f(x)) <= self.get_erro():
                print(f"\nAlgoritmo encerrado!")
                print(f"f(x) = {self.f(x)} já está próximo o suficiente.")
                print(f"Raíz aproximada encontrada em {i+1} iterações: x = {x}.")
                return

            # Calcula x da próxima iteração
            x = self.g(x)

            input()

        # Iterações finalizadas
        print(f"\nAlgoritmo encerrado!")
        print(f"Raíz aproximada encontrada em {i+1} iterações: x = {x}.")
        return


def verificaEscolha():
    escolha = int(input("\nQual será o método de busca de raízes?\n* Bisseção   (1)\n* Ponto fixo (2)\n-> "))
    while(escolha != int(1) and escolha != int(2)):
        escolha = int(input("Seleção inválida por favor tente novamente:\n* Bisseção (1)\n* Ponto fixo (2)\n-> "))
    return escolha

def main():

    escolha = verificaEscolha()

    print("\nInforme as condições iniciais:")
        
    # f(x) = (x*x*x)-9*x+5
    # g(x) = ((x*x*x)+5)/9
    # [a,b] = [0.5, 1]
    # erro = 0.01
    # iter = 8

    expressao = input("Função f(x)= ")
    x = var('x')
    funcao = sympify(expressao)
    f = lambdify(x, funcao)


    if(escolha == 2):
        expressao_ = input("Função g(x)= ")
        x = var('x')
        funcao_ = sympify(expressao_)
        g = lambdify(x, funcao_)


    print("Intervalo [a,b]")
    a = float(input("a = "))
    b = float(input("b = "))
    erro = float(input("Erro tolerado = "))
    iters = int(input("Número máximo de iterações = "))

    if(escolha == 1):
        bissecao = Bissecao(f, a, b, erro, iters)
        bissecao.executa()
    else:
        ponto_fixo = PontoFixo(f, g, a, b, erro, iters)
        ponto_fixo.executa()

if __name__ == "__main__":
    main()

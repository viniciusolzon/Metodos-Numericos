from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt

class Metodo():
    def __init__(self, f, a, b, erro, iters):
        self.f = f
        self.a = a
        self.b = b
        self.erro = erro
        self.iters = iters

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
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"\nIteração {i}")
            print(f"a = {self.get_a()}")
            print(f"b = {self.get_b()}")

            # Calcula x
            x = (self.get_a() + self.get_b()) / 2
            print(f"x = {x}")

            # Calcula f(a) e f(b)
            fa = self.f(self.get_a())
            fb = self.f(self.get_b())
            print(f"f(a) = {fa}")
            print(f"f(b) = {fb}")

            # Calcula f(x)
            fx = self.f(x)
            print(f"f(x) = {fx}")

            # Verifica se encontrou a raíz
            if fx == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz em {self.get_iters()} iterações.")
                return
            
            # Verifica o critério de erro tolerado
            if abs(fx) <= self.get_erro():
                print(f"\nAlgoritmo encerrado!")
                print(f"f(x) = {fx} já está próximo o suficiente de {self.get_erro()}.")
                return

            else:
                # Verifica se f(x) tem o mesmo sinal de f(a) ou de f(b)
                if fx * fa > 0:
                    print(f"f(x) tem o mesmo sinal de f(a)")
                    # Altera o a
                    self.set_a(x)

                else:
                    print(f"f(x) tem o mesmo sinal de f(b)")
                    # Altera o b
                    self.set_b(x)

            input()

        # Iterações finalizadas
        print(f"\nAlgoritmo encerrado!")
        print(f"Valor encontrado em {i+1} iterações: {fx}.")
        return


class PontoFixo(Metodo):
    def __init__(self, f, a, b, erro, iters):
        Metodo.__init__(self, f, a, b, erro, iters)

    def executa(self):

        print("\n* Solução *")
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"\nIteração {i}")
            print(f"a = {self.get_a()}")
            print(f"b = {self.get_b()}")

            # Isola o x pra conseguir a função de iteração
            # f_iter = 

            # A aproximação inicial de X vai ser na metade do intervalo [a,b]
            x = (self.get_a() + self.get_b()) / 2
    
            # Calcula f(x)
            fx = self.f(x)
            print(f"f(x) = {fx}")

            # Método do ponto fixo

            # Verifica se encontrou a raíz
            if fx == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz em {self.get_iters()} iterações.")
                return
            
            # Verifica o critério de erro tolerado
            if abs(fx) <= self.get_erro():
                print(f"\nAlgoritmo encerrado!")
                print(f"f(x) = {fx} já está próximo o suficiente de {self.get_erro()}.")
                return

            input()
            
        # Iterações finalizadas
        print(f"\nAlgoritmo encerrado!")
        print(f"Valor encontrado em {i+1} iterações: {fx}.")
        return



def verificaEscolha():
    escolha = int(input("\nQual será o método de busca de raízes?\n* Bisseção   (1)\n* Ponto fixo (2)\n-> "))
    while(escolha != int(1) and escolha != int(2)):
        escolha = int(input("Seleção inválida por favor tente novamente:\n* Bisseção (1)\n* Ponto fixo (2)\n-> "))
    return escolha

def main():

    escolha = verificaEscolha()
    

    print("\nInforme as condições iniciais:")
    expressao = input("Função f(x)= ")
    x = var('x')
    funcao = sympify(expressao)
    f = lambdify(x, funcao)


    print("Intervalo [a,b]")
    a = float(input("a = "))
    b = float(input("b = "))
    erro = float(input("Erro tolerado = "))
    iters = int(input("Número máximo de iterações = "))

    if(escolha == 1):
        bissecao = Bissecao(f, a, b, erro, iters)
        bissecao.executa()
    else:
        ponto_fixo = PontoFixo(f, a, b, erro, iters)
        ponto_fixo.executa()

if __name__ == "__main__":
    main()

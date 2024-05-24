from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import diff
from sympy import var

######################################## Ponto Fixo #######################################################

class PontoFixo():
    def __init__(self, f, a, b, erro, iters, g):
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
    
    def executa(self):

        print("\n* Solução *")

        # A aproximação inicial de X vai ser na metade do intervalo [a,b]
        x = (self.get_a() + self.get_b()) / 2

        for i in range(self.get_iters()):
            print(f"\nIteração {i}")
            print(f"a = {self.get_a()}")
            print(f"b = {self.get_b()}")

            print(f"x = {x}")

            # Calcula f(x)
            fx = self.f(x)
            print(f"f(x) = {fx}")

            # Verifica se encontrou a raíz
            if self.f(x) == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz x = {x} em {self.get_iters()} iterações.")
                return

            x_anterior = x

            # Calcula x da próxima iteração
            x = self.g(x)

            # Verifica o critério de erro tolerado
            if abs(x - x_anterior) <= self.get_erro():
                print(f"\nAlgoritmo encerrado!\n")
                print(f"Erro absoluto = {abs(x - x_anterior)}.")
                print(f"f(x) = {self.f(x)}.")
                print(f"Raíz aproximada encontrada em {i+1} iterações: x = {x}\n.")
                return

            input()

        # Iterações finalizadas
        print(f"\nAlgoritmo encerrado!")
        print(f"Raíz aproximada encontrada em {i+1} iterações: x = {x}.")
        return

def main():
    print("\t-Zeros de funções-")
    print("\tMétodo do Ponto Fixo")
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

    expressao_ = input("Função g(x)= ")
    x = var('x')
    funcao_ = sympify(expressao_)
    g = lambdify(x, funcao_)

    # Primeira derivada de g(x)
    dfdx = diff(funcao_,x)
    derivada = lambdify(x, dfdx)

    print("Intervalo [a,b]")
    a = float(input("a = "))
    b = float(input("b = "))

    # Verifica se g(x) é convergente:
    # primeiro critério: o módulo da derivada é < 1 para todo x pertencente ao intervalo [a,b]
    if abs(derivada(a)) > 1:
        print("Erro na escolha de g(x) ou do intervalo [a,b]")
        return

    if abs(derivada(b)) > 1:
        print("Erro na escolha de g(x) ou do intervalo [a,b]")
        return

    # segundo critério: x0 está dentro do intervalo [a,b]
    # como por padrão x0 sempre é na metade do intervalo [a,b], isso já está garantido

    erro = float(input("Erro tolerado = "))
    iters = int(input("Número máximo de iterações = "))

    ponto_fixo = PontoFixo(f, g, a, b, erro, iters)
    ponto_fixo.executa()

if __name__ == "__main__":
    main()

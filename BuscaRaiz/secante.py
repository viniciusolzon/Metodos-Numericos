from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import var

class Bissecao():
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
    def executa(self):
        print("\n* Solução *")

        x0 = self.get_a()
        x1 = self.get_b()

        for i in range(self.get_iters()):
            print(f"\nIteração {i}")
            # print(f"a = {self.get_a()}")
            # print(f"b = {self.get_b()}")

            # Calcula x
            x2 = x1 - ((self.f(x1)*(x1-x0)) /
                         (self.f(x1)-(self.f(x0))) )
            print(f"x = {x2}")

            # Calcula f(x)
            fx = self.f(x2)
            print(f"f(x) = {fx}")

            # Verifica se encontrou a raíz
            if self.f(x2) == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz x = {x2} em {self.get_iters()} iterações.")
                return
            
            # Verifica o critério de erro tolerado
            if abs(x2 - x1) <= self.get_erro():
                print(f"\nAlgoritmo encerrado!\n")
                print(f"Erro absoluto = {abs(x2 - x1)}.")
                print(f"f(x) = {self.f(x2)}.")
                print(f"Raíz aproximada encontrada em {i+1} iterações: x = {x2}\n.")
                return

            x0 = x1
            x1 = x2

            input()

        # Iterações finalizadas
        print(f"\nAlgoritmo encerrado!")
        print(f"Valor encontrado em {i+1} iterações: {fx}.")
        return


def main():

    print("\t-Zeros de funções-")
    print("\tMétodo da Secante")
    print("\nInforme as condições iniciais:")
        
    # f(x) = (x*x*x)-9*x+5
    # [a,b] = [0.5, 1]
    # erro = 0.001
    # iter = 8

    expressao = input("Função f(x)= ")
    x = var('x')
    funcao = sympify(expressao)
    f = lambdify(x, funcao)

    print("Intervalo [a,b]")
    a = float(input("a = "))
    b = float(input("b = "))

    erro = float(input("Erro tolerado = "))
    iters = int(input("Número máximo de iterações = "))

    bissecao = Bissecao(f, a, b, erro, iters)
    bissecao.executa()

if __name__ == "__main__":
    main()

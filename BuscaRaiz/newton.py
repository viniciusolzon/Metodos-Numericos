# VINICIUS FREITAS SCHIAVINATO OLZON
# MATRÍCULA 20210026803

from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import diff
from sympy import var

class Newton():
    def __init__(self, f, f_linha, a, b, erro, iters):
        self.f = f
        self.f_linha = f_linha
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

        # Calcula x
        x = (self.get_a() + self.get_b()) / 2

        if self.f_linha(1) == 0:
            print("Não satisfaz critério de convergência f'(x) != 0.")
            return

        for i in range(self.get_iters()):
            print(f"\nIteração {i}")

            print(f"x = {x}")
            x_anterior = x

            # Calcula f(x)
            fx = self.f(x)
            print(f"f(x) = {fx}")

            # Verifica se encontrou a raíz
            if self.f(x) == 0:
                print(f"\nAlgoritmo encerrado!")
                print(f"Encontrou a raíz x = {x} em {self.get_iters()} iterações.")
                return
            
            # Calcula x da próxima iteração
            fx = self.f(x)
            f_linha = self.f_linha(x)
            x = x - (fx / f_linha)

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
    print("\tMétodo de Newton")
    print("\nInforme as condições iniciais:")
        
    # f(x) = (x*x*x)-9*x+5
    # [a,b] = [0.5, 1]
    # erro = 0.01
    # iter = 8

    expressao = input("Função f(x)= ")
    x = var('x')
    funcao = sympify(expressao)
    f = lambdify(x, funcao)

    dfdx = diff(funcao,x)
    f_linha = lambdify(x, dfdx)

    print("Intervalo [a,b]")
    a = float(input("a = "))
    b = float(input("b = "))

    erro = float(input("Erro tolerado = "))
    iters = int(input("Número máximo de iterações = "))

    newton = Newton(f, f_linha, a, b, erro, iters)
    newton.executa()

if __name__ == "__main__":
    main()

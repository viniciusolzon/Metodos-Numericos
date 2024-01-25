
def PontoFixo():
    pass


def Bissecao():
    pass

def verificaEscolha():
    choice = int(input("\nQual será o método de busca de raízes?\n* Bisseção (1)\n* Ponto fixo (2)\n-> "))
    while(choice != int(1) and choice != int(2)):
        choice = int(input("Seleção inválida por favor tente novamente:\n* Bisseção (1)\n* Ponto fixo (2)\n-> "))
    return choice

def main():

    print("\nInforme as condições iniciais:")
    function = input("Função(xi,yi) = ")
    yi = float(input("Valor inicial de y = "))
    xi = float(input("Valor inicial de x = "))
    h = float(input("Valor de h = "))
    iters = int(input("Número de iterações = "))

    f = lambda xi, yi: eval(function)

    choice = verificaEscolha()
    if(choice == 1):
        euler = Bissecao(f, yi, xi, h, iters)
        euler.solve()
        euler.plotGraph()
    else:
        rk4 = PontoFixo(f, yi, xi, h, iters)
        rk4.solve()
        rk4.plotGraph()


if __name__ == "__main__":
    main()

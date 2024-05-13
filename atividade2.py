# VINICIUS FREITAS SCHIAVINATO OLZON
# MATRÍCULA 20210026803

import matplotlib.pyplot as plt
import numpy as np

######################################## LU #######################################################

class FatoracaoLU():
    def __init__(self, A):
        self.A = A
        self.n = len(A)
        # Instancia a matriz L sendo uma matriz idêntidade na mesma ordem de A
        self.L = np.identity(self.n)
        # Instancia a matriz U sendo uma matriz cópia de A, depois iremos alterar abaixo da diagonal para 0
        self.U = self.A.copy()

    def solve(self):
        ordem = self.n
        for i in range(ordem-1):
            if self.U[i][i] != 0:# Só funciona se a matriz A não tiver diagonal igual a 0

                for j in range(i+1, ordem): # Atualiza matriz L e deixa U de forma correta agora
                    self.L[j][i] = self.U[j][i]/self.U[i][i]
                    self.U[j][i] = 0

                    for k in range(i+1, ordem): # Atualiza matriz U
                        self.U[j][k] = self.U[j][k] - self.L[j][i]*self.U[i][k]
            else:
                print("Nao possui decomposicao LU")

        return self.L, self.U

def printMatrix(matriz, n, m):
    for i in range(n):

        for j in range(m):
            print(f'{matriz[i][j]:.4f}', end = " ")
        print("\n")

def mostra_LU():
    print("\t-Fatoração LU-")
    print("\nInforme a matriz A.")
    qtd_linhas = int(input("  Quantidade de linhas: "))
    qtd_colunas = int(input("  Quantidade de colunas: "))
    A = []
    for i in range(qtd_linhas):
        a =[]
        for j in range(qtd_colunas):
            a.append(int(input(f"A[{i}][{j}] = ")))
        A.append(a)

    # Printando a matriz
    print("\nMatriz A:")
    printMatrix(A, qtd_linhas, qtd_colunas)

    fatoracao = FatoracaoLU(A)
    L, U = fatoracao.solve()

    # Printando as matrizes L e U
    print("\nMatriz L:")
    printMatrix(L, qtd_linhas, qtd_colunas)
    print("\nMatriz U:")
    printMatrix(U, qtd_linhas, qtd_colunas)

    # Matriz A para teste = [[3,2,4],[1,1,2],[4,3,-2]]
    # Matriz L esperada = [[1,0,0],[0.3333,1,0],[1.3333,1,1]]
    # Matriz U esperada = [[3,2,4],[0,0.3333,0.6666],[0,0,-8]]


######################################## THOMAS ###################################################

class Thomas():
    def __init__(self, ds, dp, di, b):
        self.b = b
        self.n = len(b)
        self.ds = ds
        self.dp = dp
        self.di = di

    def solve(self):
        self.x = np.zeros(self.n)

        c5 = np.zeros(self.n-1)
        c2 = np.zeros(self.n)

        for i in range(self.n):
            if i == 0:
                c5[i] = self.di[i]/self.dp[i]
                c2[i] = self.b[i]/self.dp[i]
            elif i == self.n-1:
                c2[i] = (self.b[i]-self.ds[i]*c2[i-1])/(self.dp[i]-self.ds[i]*c5[i-1])
            else:
                c5[i] = self.di[i]/(self.dp[i]-self.ds[i]*c5[i-1])
                c2[i] = (self.b[i]-(self.ds[i]*c2[i-1]))/(self.dp[i]-self.ds[i]*c5[i-1])

        # Executa o cálculo de X
        self.x[-1] = round(c2[-1], 5)
        for i in range(self.n-2, -1, -1):
            self.x[i] = round(c2[i]-c5[i]*self.x[i+1], 5)
            
        return self.x


def mostra_Thomas():

    print("\t-Algoritmo de Thomas-")

    b_len = int(input("\nInforme a quantidade de elementos do vetor b: "))
    b = []
    for i in range(b_len):
        b.append(int(input("Elementos do vetor b = ")))

    ds = []
    print()
    for i in range(b_len):
        ds.append(int(input("Elementos da diagonal superior = ")))

    dp = []
    print()
    for i in range(b_len):
        dp.append(int(input("Elementos da diagonal principal = ")))

    di = []
    print()
    for i in range(b_len):
        di.append(int(input("Elementos da diagonal inferior = ")))

    print(f"\nDiagonal superior: {ds}")
    print(f"\nDiagonal principal: {dp}")
    print(f"\nDiagonal inferior: {di}")

    thomas = Thomas(ds, dp, di, b)
    x = thomas.solve()
    print(f"\nVetor X = {x}")

    # Diagonal superior para teste = [0,1,1,1,1]
    # Diagonal principal para teste = [2,2,2,2,2]
    # Diagonal inferior para teste = [1,1,1,1,0]
    # Vetor b para teste = [4, 4, 0, 0, 2]
    # X esperado = [1, 2, -1, 0, 1]

######################################## GAUSS_SEIDEL #############################################

class GaussSeidel():
    # Melhoria do processo iterativo de Jacobi
    def __init__(self, A, b, vetorsolucao, iteracoes = 10, erro_tolerado = 1e-10):
        self.A = A
        self.b = b
        self.iteracoes = iteracoes
        self.vetorsolucao = vetorsolucao
        self.erro_tolerado = erro_tolerado

    def solve(self):
        print(self.A)
        print(self.b)
        print(self.vetorsolucao)
        iteracao = 0
        erro = 1
        x = 0

        # Executa até o máximo de iterações permitidas ou até atinigir o erro tolerado
        while iteracao < self.iteracoes and erro >= self.erro_tolerado:
            for i in range(len(self.A)):
                x = self.b[i]
                for j in range(len(self.A)):
                    if i!=j:
                        x-=self.A[i][j]*self.vetorsolucao[j]
                x/= self.A[i][i]
                self.vetorsolucao[i] = x

            # Verifica critério de parada por erro tolerado
            erro = np.max(np.abs(self.vetorsolucao- x))/np.max(np.abs(self.vetorsolucao))
            iteracao+=1

        return self.vetorsolucao
    
def mostra_Gauss_Seidel():
    print("\t-Método de Gauss Seidel-")
    gauss_seidel = GaussSeidel(np.array([[2,1], [2,4]]), np.array([5, 11]), np.array([0,0]))
    x = gauss_seidel.solve()
    print(f"\nVetor X = {x}")

    # Matriz A para teste = [[2,1],[2,4]]
    # Vetor b para teste = [5,11]
    # Vetor x inicial para teste = [0,0]
    # x final esperado = [2,1]
    
######################################## INTERPOLAÇÃO_LAGRANGE #############################################

class InterpolacaoLagrange():
    def __init__(self, x, y, grau):
        self.x = x
        self.y = y
        self.n = grau

    # Procura o polinômio interpolador a partir de 3 pontos dados
    def solve(self, xp):
        yp = 0
        for i in range(0, self.n+1):
            p = 1
            for j in range(0, self.n+1):
                if i != j:
                    p = p*(xp - self.x[j])/(self.x[i] - self.x[j])
            yp = yp + p * self.y[i]

        return yp

def mostra_Interpolacao_Lagrange():
    print("\t-Interpolação de Lagrange-")
    x = np.array([-1,0,2])
    y = np.array([4,1,-1])
    grau = 2
    xp = 1.5
    
    il = InterpolacaoLagrange(x, y, grau)
    yp = il.solve(xp)
    
    t = np.arange(-1, 2, 0.1)
    yt = []
    for i in t:
        yt.append(il.solve(i))

    # Plotando o gráfico do polinômio interpolador e o ponto dado
    plt.plot(t, yt, 'b-')
    plt.plot(x, y, 'ro')
    plt.plot(xp, yp, 'g*')
    plt.show()

######################################## Demonstrações ############################################

def main():
    # mostra_LU()
    # mostra_Thomas()
    # mostra_Gauss_Seidel()
    # mostra_Interpolacao_Lagrange()
    pass

if __name__ == "__main__":
    main()

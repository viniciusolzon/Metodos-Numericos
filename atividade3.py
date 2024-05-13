# VINICIUS FREITAS SCHIAVINATO OLZON
# MATRÍCULA 20210026803

import numpy as np
import matplotlib.pyplot as plt

######################################## 1/3 SIMPSON #############################################

class UmTercoSimpson():
    def __init__(self, a, b, n):
        self.h = (b-a)/n
        self.a = a
        self.b = b
        self.n = n
        
    def f(self, x):
        return 1/(1+x)

    def solve(self):
        soma = 0
        iter = 1
        while iter < self.n:
            x = self.a+iter*self.h
            if (iter)%2 == 0:
                soma+= 2*self.f(x)
            else:
                soma+= 4*self.f(x)
            iter+=1

        integral_aproximada = (self.h/3) * (self.f(self.a) + self.f(self.b) + soma)
        return integral_aproximada

def mostra_UmTercoSimpson():
    print("\t-1/3 Simpson-")
    a = float(input("Limite inferior da integral: "))
    b = float(input("Limite superior da integral: "))
    n = int(input("Subintervalos: "))
    um_terco_simpson = UmTercoSimpson(a,b,n)
    integral_aproximada = um_terco_simpson.solve()
    print(f"Valor aproximado da integração: {integral_aproximada}")

######################################## 1/3 SIMPSON #############################################

class MMQ():
    def __init__(self, x, y_lin, y_quad):
        self.x = x
        self.y_lin = y_lin
        self.y_quad = y_quad
        self.n = len(x)

    def solve(self, metodo, y):
        # Usuário escolheu método linear
        if metodo == 1:
            x_sum = np.sum(self.x)
            y_sum = np.sum(y)
            x_squared_sum = np.sum(self.x ** 2)
            xy_sum = np.sum(self.x*y)

            b1 = (self.n*xy_sum - x_sum*y_sum) / (self.n*x_squared_sum - x_sum**2)
            b0 = (y_sum - b1*x_sum) / self.n

            return b0, b1

        # Usuário escolheu método linear
        elif metodo == 2:
            n = len(self.x)
            x_sum = np.sum(self.x)
            x_squared_sum = np.sum(self.x ** 2)
            x_cubed_sum = np.sum(self.x ** 3)
            x_quad_sum = np.sum(self.x ** 4)

            y_sum = np.sum(y)
            xy_sum = np.sum(self.x*y)
            x_squared_y_sum = np.sum(self.x**2 * y)

            A = np.array([[n, x_sum, x_squared_sum],[x_sum, x_squared_sum, x_cubed_sum],[x_squared_sum, x_cubed_sum, x_quad_sum]])
            
            b = np.array([y_sum, xy_sum, x_squared_y_sum])
            b0, b1, b2 = np.linalg.solve(A, b)

            return b0, b1, b2

    def solver_lin(self, y):
        return self.solve(1, y)
    
    def solver_quad(self, y):
        return self.solve(2, y)

    def f_lin(self, y):
        b, a = self.solve(1, y)
        return [a*x + b for x in self.x]

    def f_quad(self, y):
        c, b, a = self.solve(2, y)
        return [a*x**2 + b*x + c for x in self.x]
    
    def view_lin(self, y):
        ax = plt.gca()
        ax.plot(self.x, y, 'ro')
        ax.plot(self.x, self.f_lin(y), 'b-')
        ax.set_xlabel('x')
        ax.set_ylabel('y', rotation=0)
        return ax

    def view_quad(self, y):
        ax = plt.gca()
        ax.plot(self.x, y, 'ro')
        ax.plot(self.x, self.f_quad(y), 'b-')
        ax.set_xlabel('x')
        ax.set_ylabel('y', rotation=0)
        return ax


    def view(self, view : str = 'all', y : list = []):
        if view == 'lin':
            ax = self.view_lin(y)
            ax.set_title('Reta linear com ajuste Linear')
            plt.show()

        if view == 'quad':
            ax = self.view_quad(y)
            ax.set_title('Curva quadratica com Ajuste Quadratico')
            plt.show()
        
        if view == 'all':
            fig, axes = plt.subplots(2, 2, figsize=(12, 6))  # Create figure and 2x2 subplots

            axes[0, 0].plot(self.x, self.y_lin, 'ro', label='Original Data') 
            axes[0, 0].plot(self.x, self.f_lin(self.y_lin), 'b-', label='Linear Fit')
            axes[0, 0].set_xlabel('x')
            axes[0, 0].set_ylabel('y')
            axes[0, 0].set_title('Reta linear com Ajuste Linear')  

            axes[0, 1].plot(self.x, self.y_lin, 'ro', label='Original Data') 
            axes[0, 1].plot(self.x, self.f_quad(self.y_lin), 'b-', label='Quadratic Fit')  
            axes[0, 1].set_xlabel('x')
            axes[0, 1].set_ylabel('y')
            axes[0, 1].set_title('Reta linear com Ajuste Quadrático')  

            axes[1, 0].plot(self.x, self.y_quad, 'ro', label='Original Data')  
            axes[1, 0].plot(self.x, self.f_lin(self.y_quad), 'b-', label='Linear Fit')  
            axes[1, 0].set_xlabel('x')
            axes[1, 0].set_ylabel('y')
            axes[1, 0].set_title('Curva Quadratica com Ajuste Linear') 

            axes[1, 1].plot(self.x, self.y_quad, 'ro', label='Original Data')  
            axes[1, 1].plot(self.x, self.f_quad(self.y_quad), 'b-', label='Quadratic Fit')  
            axes[1, 1].set_xlabel('x')
            axes[1, 1].set_ylabel('y')
            axes[1, 1].set_title('Curva Quadratica com Ajuste Quadratico') 

            fig.tight_layout()
            plt.show()


def linf(x):
    return 2*x + 15

def quadf(x):
    return 2*x**2 + 3*x + 15

def mostra_MMQ():
    print("\t-Método de Mínimos Quadrados Linear e Quadrático-")
    x = np.linspace(0, 10, 10)
    y_lin = np.array([linf(i) for i in x])
    y_quad = np.array([quadf(i) for i in x])
    # Instancia a classe de MMQ
    mmq = MMQ(x, y_lin, y_quad)
    # Plota o gŕafico dos ajustes lineares e quadráticos
    mmq.view('all')

######################################## Demonstrações ############################################

def main():
    # mostra_UmTercoSimpson()
    mostra_MMQ()

if __name__ == "__main__":
    main()

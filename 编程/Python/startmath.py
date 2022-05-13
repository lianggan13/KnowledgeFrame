import numpy as np
import matplotlib.pyplot as plt
import sympy as sp 


# x=np.linspace(0,5,1000)
# y=x**2
# plt.figure()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(x,y,label="$y=x^2$")

# plt.legend()
# x=np.linspace(0,5,1000)

# for i in x:
#     x_z=[]
#     y_z=[]
#     x_z.append(i)
#     y_z.append(0) 
#     x_z.append(i)
#     y_z.append(i**2)
#     plt.plot(x_z,y_z)
#     plt.show()

x, y, z, a, b, c = sp.symbols('x, y, z, a, b, c')

def Limit():
    fx = (x+1)**2  + 1 # x-> a-1
    v = sp.limit(fx,x,a-1)
    print(v)

    fx = sp.sin(x)/x
    v =sp.limit(fx,x,0)
    print(v)
    v = sp.limit(fx,x,0,dir="-")
    print(v)

    Δx = sp.Symbol('Δx')
    fx = sp.cos(x) # f(x) = cosx
    fx_a = sp.limit(fx,x,a) # f(a)
    fx_aΔx = sp.limit(fx,x,a-Δx) # f(a - Δx)
    f = sp.limit((fx_a - fx_aΔx)/Δx,Δx,0) # Δx --> 0
    print(f)

    n = sp.Symbol('n')
    f = sp.limit( ((n+3) / (n+2))**n,n,sp.oo) 
    print(f)

    
def Diff():
    print(sp.diff(sp.sin(2*x), x, 3))

def Dsolve():
    x = sp.symbols("x", real=True) # 定义符号x 为实数 
    eq1 = sp.dsolve(sp.f(x).diff(x) + sp.f(x)**2 + sp.f(x), sp.f(x)) 
    print(eq1)

def Intergrate():
    print("Intergrate:")

    f = sp.exp(x)
    v = sp.integrate(f,(x,-sp.oo,0))
    print(v)

    f = 3*x**2 + 1
    v = sp.integrate(f,x)
    print(v)

    f = (4/3)*x + 2*y
    v = sp.integrate(f,(x,0,1),(y,-3,4))
    print(v)

    v = sp.integrate(f,(x,0,1),(y,-x,x))
    print(v)

if __name__ == "__main__":
    Limit()
    Diff()
    # Dsolve()
    Intergrate()
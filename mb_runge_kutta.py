import math
import numpy as np
import plotly.express as px

# Initial parameters of the market
while True:
    try:
        print("\nInitial parameters of the market ")
        c_u = int(input("Input u: "))
        c_v = int(input("Input v: "))
        alfa = int(input("Input Alfa: "))
        beta = int(input("Input Beta: "))
        delta = int(input("Input Delta: "))
        break

    except:
        print("\nError DataType. Please input a valid numer\n")

# Initial parameters for the model
while True:   
    try:
        print("\nInitial parameters for the model ")
        y = int(input("Input y(0): "))
        z = int(input("Input y'(0): "))
        limit = int(input("Input limit: "))
        break

    except:
        print("\nError DataType. Please input a valid numer\n")

# Learning rate
h = 0.01

# factors
a1 = c_u/c_v
a2 = -(beta+delta)/c_v
a3 = -(alfa+delta)/c_v

# x, y arrays
x_list = [i*h for i in range(int(math.ceil(limit/h)))]
y_list = []

func = lambda z, y: a3 - a1*z - a2*y 

# Runge–Kutta
for x in x_list:
    y_list.append(y)
    
    m1 = h*z
    k1 = h* func(z, y)
    m2 = h*(z + h*k1)
    k2 = h*func(z + h*k1, y + h*h)
    m3 = h*(z + h*k2)
    k3 = h*func(z + z*k2, y + h*h)
    m4 = h*(z + k3)
    k4 = h*func(z+k3, y+h)

    y += (1/6)*(m1 + 2*m2 + 2*m3 + m4)
    z += (1/6)*(k1 + 2*k2 + 2*k3 + k4)

# Graph
fig = px.line(x=x_list, y=y_list, title='Runge–Kutta')
fig.show()
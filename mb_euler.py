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

# x, y, z arrays
x_list = [0]
y_list = [y]
z_list = [z]

func = lambda z, y: a3 - a1*z - a2*y 

for i in range(int(math.ceil(limit/h))):
    x_list.append(x_list[i] + h)
    y_list.append(y_list[i] + h*z_list[i])
    z_list.append(z_list[i] + h*func(z_list[i],y_list[i]))

# Graph
fig = px.line(x=x_list, y=y_list, title='Euler')
fig.show()
    
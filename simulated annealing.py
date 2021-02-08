import random
import math
import matplotlib.pyplot as plt

def func_cal(function, x, y):
    if function == "Sphere":
        f1 = (x)**2 + (y)**2
    elif function == "Rosenbrock":
        f1 = 100*(x**2 - y)**2 + (1-x)**2
    else:
        f1 = ((x**2+y**2)/4000)-math.cos(x)*math.cos(y/sqrt(2))+1
    return f1

def find_neighbor(x, y, step):
    neighbor_lst = []
    neighbor_lst.append((x+0.5, y))
    neighbor_lst.append((x, y+0.5))
    neighbor_lst.append((x+0.5, y+0.5))
    neighbor_lst.append((x-0.5, y))
    neighbor_lst.append((x, y-0.5))
    neighbor_lst.append((x-0.5, y-0.5))
    neighbor_lst.append((x-0.5, y+0.5))
    neighbor_lst.append((x+0.5, y-0.5))
    return neighbor_lst

def SimulatedAnnealing(function, optima, temp, x1, x2, y1, y2, step, decay):
    x3 = random.uniform(x1, x2)
    y3 = random.uniform(y1, y2)
    f1 = func_cal(function, x3, y3)
    visited = []
    x_lst = []
    y_lst = []
    f1_lst = []
    j = -1
    while (temp != 0):
        for i in range(50):
            if j == 7:
                break
            else:
                j+=1
            neighbor_lst = find_neighbor(x3, y3, step)
            x4, y4 = neighbor_lst[j]
            f2 = func_cal(function, x4, y4)
            if (optima == "max"):
                if (f2 > f1):
                    f1 = f2
                    x3, y3 = x4, y4
                    visited = []
                    x_lst.append(x3)
                    y_lst.append(y3)
                    f1_lst.append(f1)
                    j = 0
                else:
                    prob = math.exp((f2 - f1)/temp)
                    rand = random.uniform(0,1)
                    if (rand < prob):
                        f1 = f2
                        x3, y3 = x4, y4
                        visited = []
                        x_lst.append(x3)
                        y_lst.append(y3)
                        f1_lst.append(f1)
                        j = 0
                    else:
                        continue
            else:
                if (f2 < f1):
                    f1 = f2
                    x3, y3 = x4, y4
                    visited = []
                    x_lst.append(x3)
                    y_lst.append(y3)
                    f1_lst.append(f1)
                    j = 0
                else:
                    prob = math.exp((f1 - f2)/temp)
                    rand = random.uniform(0,1)
                    if (rand < prob):
                        f1 = f2
                        x3, y3 = x4, y4
                        visited = []
                        x_lst.append(x3)
                        y_lst.append(y3)
                        f1_lst.append(f1)
                        j = 0
                    else:
                        continue
        if (j==8):
            break
        else:
            temp = temp*0.2
    return x3, y3, f1_lst, x_lst, y_lst

function = input("Enter function name: ")
if function == "Sphere":
    x1, x2 = -5, 5
    y1, y2 = -5, 5
elif function == "Rosenbrock":
    x1, x2 = -2, 2
    y1, y2 = -1, 3
else:
    x1, x2 = -10, 10
    y1, y2 = -10, 10
max_min = "min"
temp = 1
step = 0.1
decay = 0.95
x, y, f1_lst, optima_x, optima_y = SimulatedAnnealing(function, max_min, temp, x1, x2, y1, y2, step, decay)
plt.plot(optima_x)
plt.plot(optima_y)
plt.plot(f1_lst)
plt.legend(["x", "y", "f1"])
plt.show()
print(x, y)

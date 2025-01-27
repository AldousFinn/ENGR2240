#Huxley Rust
#27/01/2025
#ENGR2240


import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols



def x_prime_loop (x_value, y_value):
    substitutions = {x: x_value, y: y_value}
    slope = diff_eq.subs(substitutions)
    return slope

def solved_diff_eq_loop (x_value):
    substitutions = {x: x_value}
    solved_y_value = solved_diff_eq.subs(substitutions)
    return solved_y_value

x, y = symbols('x y')
diff_eq = sympify(input("What is the Diff. Eq. (dy/dx form)? "))
solved_diff_eq = sympify(input("What is the solved Diff. Eq. (y = f(x,y) form)? "))
x_initial = float(input("What is the initial 'x' value? "))
x_final = float(input("What is the final 'x' value? "))
y_initial = float(input("What is the initial 'y' value? "))
number_steps = int(input("What number of steps should there be for the first equation? "))
number_steps_two = int(input("What number of steps should there be for the second equation? "))
number_steps_three = int(input("What number of steps should there be for the third equation? "))
dpi_set = int(input("What should the DPI of the graph be? "))


slope_initial = x_prime_loop(x_initial, y_initial)
x_prime_nought = (x_final - x_initial) / number_steps
x_prime_nought_two = (x_final - x_initial) / number_steps_two
x_prime_nought_three = (x_final - x_initial) / number_steps_three
x_values = np.linspace(x_initial, x_final, number_steps)
y_values = np.zeros(number_steps)
y_values_two = np.zeros(number_steps_two)
y_values_three = np.zeros(number_steps_three)
solved_y_values = np.zeros(number_steps)
slope = np.zeros(number_steps)


y_values[0] = y_initial
solved_y_values[0] = y_initial
slope[0] = slope_initial


for ii in range(1, number_steps):
    y_values[ii] = y_values[ii - 1] + (x_prime_nought * x_prime_loop(x_values[ii-1], y_values[ii-1]))
    solved_y_values[ii] = solved_diff_eq_loop(x_values[ii])

for ii in range(1, number_steps_two):
    y_values_two[ii] = y_values[ii - 1] + (x_prime_nought_two * x_prime_loop(x_values[ii-1], y_values[ii-1]))
    
for ii in range(1, number_steps_three):
    y_values_three[ii] = y_values[ii - 1] + (x_prime_nought_three * x_prime_loop(x_values[ii-1], y_values[ii-1]))


plt.figure(1, dpi = dpi_set)
plt.plot(x_values, y_values,'.-m', markerfacecolor = 'green', markeredgecolor = 'green')
if solved_diff_eq != 0:
    plt.plot(x_values, solved_y_values, '.-r', markerfacecolor = 'blue', markeredgecolor = 'blue')
    plt.fill_between(x_values, y_values, solved_y_values, color = 'gray', alpha=0.3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
title = f"Solution of Differential Equation through y({x_initial}) = {y_initial}"
plt.title(title)
plt.show()


#=====================================================================================================#


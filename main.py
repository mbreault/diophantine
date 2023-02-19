from sympy.solvers.diophantine import diophantine
from sympy.abc import x, y, z
from sympy import simplify
from sympy.solvers.diophantine.diophantine import diop_DN


def problem1(D):
  solutions = {}
  max_x = 0
  max_y = 0
  max_z = 0
  for i in range(1, D):
    solutions[i]= diop_DN(i, 1) # Solves equation x**2 - 13*y**2 = -4

  for z, xy_pairs in solutions.items():
    for x, y in xy_pairs:
        if x > max_x:  # if we've found a new maximum value of x
            max_x = x  # update the maximum value of x
            max_y = y  # update the corresponding value of y
            max_z = z  # update the corresponding value of z

  print(f"Maximum value of x is {max_x} is obtained when D = {max_z}")


def main():
    
  # Example usage
  D = 1000
  max_x = 10**10  # Set to a large value to find all solutions
  problem1(D)

if __name__ == '__main__':
    main()

import sympy as sp
import scipy.integrate as spi
import numpy as np

def get_user_function():
    while True:
        print("Enter a mathematical function in temrs of \"x\"")
        user_function = input("f(x) = ")

        try:
            user_function = sp.sympify(user_function)
            return sp.sympify(user_function)
        except:
            print("Invalid mathematical function")

def get_user_interval():
    while True:
        left_endpoint = input("Enter the left endpoint: ")
        right_endpoint = input("Enter the right endpoint: ")

        try:
            left_endpoint = float(left_endpoint)
            right_endpoint = float(right_endpoint)

            if left_endpoint < right_endpoint:
                return left_endpoint, right_endpoint
            else:
                print("Left endpoint must be less than right endpoint.")
        except ValueError:
            print("Please enter a valid interval.")

def get_user_polynomial_degree():
    MIN_DEGREE = 2
    MAX_DEGREE = 5
    
    while True:
        degree = input(f"Please enter the degree of the polynomial approximation ({MIN_DEGREE}-{MAX_DEGREE}): ")

        try:
            degree = int(degree)

            if MIN_DEGREE <= degree <= MAX_DEGREE:
                return degree
            else:
                print(f"Degree must be between {MIN_DEGREE} and {MAX_DEGREE}")
        except ValueError:
            print("Please enter a valid number")

x = sp.symbols("x")

def legendre_polynomial(degree):
    return sp.lambdify(x, sp.legendre(degree, x), "numpy")

def calculate_approximation(function, degree, left_endpoint, right_endpoint):
    t = (2*x - left_endpoint - right_endpoint)/(right_endpoint - left_endpoint)
    
    polynomial = 0

    f_numeric = sp.lambdify(x, function, "numpy")
    t_numeric = sp.lambdify(x, t, "numpy")

    for i in range(degree + 1):
        P_i_sym = sp.legendre(i, t)
        P_i_num = sp.lambdify(x, P_i_sym, "numpy")

        integrand = lambda s: f_numeric(s) * P_i_num(s)

        integral, _ = spi.quad(integrand, left_endpoint, right_endpoint)

        coefficient = (2*i + 1)/(right_endpoint - left_endpoint)

        polynomial += coefficient * integral * P_i_sym
    
    return sp.simplify(polynomial)

def main():
    f = get_user_function()
    left_endpoint, right_endpoint = get_user_interval()
    n = get_user_polynomial_degree()

    approximation = calculate_approximation(f, n, left_endpoint, right_endpoint)

    print("Legenre least-squares approximation:")
    print(approximation)

main()
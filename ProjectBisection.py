import tkinter as tk
import math
from tkinter import messagebox
from sympy import Symbol,diff, sympify, sin, cos, tan

#Bisection
def evaluate_function(equation, x):
    try:
        expr = sympify(equation)
        expr = expr.subs(Symbol('sin'), sin)
        expr = expr.subs(Symbol('cos'), cos)
        expr = expr.subs(Symbol('tan'), tan)
        return expr.subs(Symbol('x'), x)
        result = equation.subs('x', x)
        return result
    except:
        messagebox.showerror("Error", "Invalid equation")
        return None
     
    
#Regula Falsi
def evaluate_equation(equation, x):
    try:
        expr = sympify(equation)
        expr = expr.subs(Symbol('sin'), sin)
        expr = expr.subs(Symbol('cos'), cos)
        expr = expr.subs(Symbol('tan'), tan)
        return expr.subs(Symbol('x'), x)
    except:
        messagebox.showerror("Error", "Invalid equation")
        return None 

#Bisection
def bisection_method(equation, a, b, tolerance):
    fa = evaluate_function(equation, a)
    fb = evaluate_function(equation, b)

    if fa is None or fb is None:
        return None

    if fa * fb > 0:            #its mean the interval does not contain a root
        messagebox.showerror("Error", "Function values at 'a' and 'b' should have opposite signs")
        return None

    while abs(b - a) > tolerance:           # c = mid point value
        c = (a + b) / 2
        fc = evaluate_function(equation, c)

        if fc is None:
            return None

        if abs(fc) <= tolerance:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2


#Regula Falsi
def regula_falsi_method(equation, a, b, tolerance, max_iterations):
    fa = evaluate_equation(equation, a)
    fb = evaluate_equation(equation, b)

    if fa is None or fb is None:
        return None

    if fa * fb > 0:
        messagebox.showerror("Error", "Function values at 'a' and 'b' should have opposite signs")
        return None

    for iteration in range(max_iterations):
        c = (a * fb - b * fa) / (fb - fa)
        fc = evaluate_equation(equation, c)

        if fc is None:
            return None

        if abs(fc) <= tolerance:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    messagebox.showwarning("Warning", "Maximum iterations exceeded")
    return None

#Newton Raphson
def newton_raphson_method(equation, initial_guess, tolerance, max_iterations):
    x = initial_guess

    for iteration in range(max_iterations):
        f = evaluate_equation(equation, x)
        df = diff(equation, Symbol('x')).subs(Symbol('x'), x)

        if f is None or df is None:
            return None

        if abs(f) <= tolerance:
            return x

        if df == 0:
            messagebox.showerror("Error", "Derivative is zero")
            return None

        x = x - f / df

    messagebox.showwarning("Warning", "Maximum iterations exceeded")
    return None

#Bisection
def calculate():
    equation_str = equation_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    tolerance = float(tolerance_entry.get())

    try:
        equation = sympify(equation_str)
        result = bisection_method(equation, a, b, tolerance)

        if result is not None:
            result_label.config(text=f"Root: {result}")
    except:
        messagebox.showerror("Error", "Invalid equation")

#Regula Falsi Calculation
def calculateR():
    equation = equation_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    tolerance = float(tolerance_entry.get())
    max_iterations = int(max_iterations_entry.get())

    result = regula_falsi_method(equation, a, b, tolerance, max_iterations)

    if result is not None:
        result_label.config(text=f"Root: {result}")


#Newton Calculation
def calculateN():
    equation = equation_entry.get()
    initial_guess = float(initial_guess_entry.get())
    tolerance = float(tolerance_entry.get())
    max_iterations = int(max_iterations_entry.get())

    result = newton_raphson_method(equation, initial_guess, tolerance, max_iterations)

    if result is not None:
        result_label.config(text=f"Root: {result}")


###############################################################################
# Create the main window
window = tk.Tk()
window.title("Roots With Different Methods")
window.geometry("350x250")
window.configure(bg='#588157')
#Toplevel Window
def OpenBisection():    
    global label
    global result_label
    global max_iterations_entry
    global tolerance_entry
    global a_entry
    global b_entry
    global equation_entry
    global btnEx
    global top
    
    top = tk.Toplevel()
    top.title('Bisection')
    top.geometry("400x330")
    top.configure(bg='#74886C')
    label = tk.Label(top, text='This is Bisection')
    #Create equation label and entry
    equation_label = tk.Label(top, text="Equation:",bg='#74886C',fg='#A01808',font=('Medya'))
    equation_label.pack(pady = 5)
    equation_entry = tk.Entry(top)
    equation_entry.pack(pady = 2)

    # Create 'a' label and entry
    a_label = tk.Label(top, text="a:",bg='#74886C',fg='#A01808',font=('Helvetica'))
    a_label.pack(pady = 5)
    a_entry = tk.Entry(top)
    a_entry.pack(pady = 2)

    # Create 'b' label and entry
    b_label = tk.Label(top, text="b:",bg='#74886C',fg='#A01808',font=('Helvetica'))
    b_label.pack(pady = 5)
    b_entry = tk.Entry(top)
    b_entry.pack(pady = 2)

    # Create tolerance label and entry
    tolerance_label = tk.Label(top, text="Tolerance:",bg='#74886C',fg='#A01808',font=('Helvetica'))
    tolerance_label.pack(pady = 5)
    tolerance_entry = tk.Entry(top)
    tolerance_entry.pack(pady = 2)

    # Create the calculate button
    calculate_button = tk.Button(top, text="Calculate", command=calculate,bg='#74886C',fg='#A01808',font=('Helvetica'))
    calculate_button.pack(pady = 5)

    # Create the result label
    result_label = tk.Label(top, text="")
    result_label.pack(pady = 2)
    
    btnEx = tk.Button(top, text = 'Exit', command = topdestroy,bg='#74886C',fg='#A01808',font=('S')).pack(pady = 5)
###############################################################################


###############################################################################
def RegulaExample():
    global label
    global result_label
    global max_iterations_entry
    global tolerance_entry
    global a_entry
    global b_entry
    global equation_entry
    global btnEx
    global top2
    global equation_label
    
    top2 = tk.Toplevel()
    top2.title('Regula Falsi')
    top2.geometry("400x370")
    top2.configure(bg='#fdfcdc')
    # label = tk.Label(top2, text = 'This is Regula Falsi').pack()
    #Regula
    equation_label = tk.Label(top2, text="Equation:",bg='#fdfcdc',fg='#00afb9')
    equation_label.pack(pady=5)
    equation_entry = tk.Entry(top2,bg='#fed9b7')
    equation_entry.pack(pady=2)

    # Create 'a' label and entry
    a_label = tk.Label(top2, text="a:",bg='#fdfcdc',fg='#00afb9')
    a_label.pack(pady=5)
    a_entry = tk.Entry(top2,bg='#fed9b7')
    a_entry.pack(pady=2)

    # Create 'b' label and entry
    b_label = tk.Label(top2, text="b:",bg='#fdfcdc',fg='#00afb9')
    b_label.pack(pady=5)
    b_entry = tk.Entry(top2,bg='#fed9b7')
    b_entry.pack(pady=2)

    # Create tolerance label and entry
    tolerance_label = tk.Label(top2, text="Tolerance:",bg='#fdfcdc',fg='#00afb9')
    tolerance_label.pack(pady=5)
    tolerance_entry = tk.Entry(top2,bg='#fed9b7')
    tolerance_entry.pack(pady=2)

    # Create maximum iterations label and entry
    max_iterations_label = tk.Label(top2, text="Maximum Iterations:",bg='#fdfcdc',fg='#00afb9')
    max_iterations_label.pack(pady=5)
    max_iterations_entry = tk.Entry(top2,bg='#fed9b7')
    max_iterations_entry.pack(pady=2)

    # Create the calculate button
    calculate_button = tk.Button(top2, text="Calculate", command=calculateR,bg='#fdfcdc',fg='#00afb9')
    calculate_button.pack(pady=5)

    # Create the result label
    result_label = tk.Label(top2, text="")
    result_label.pack(pady=5)
    
    btnEx = tk.Button(top2, text = 'Exit', command = top2destroy,bg='#fed9b7').pack(pady=5)
###############################################################################

###############################################################################    
def NewtonRaphson():
    global top3
    global initial_guess_entry
    global result_label
    global max_iterations_entry
    global tolerance_entry
    global a_entry
    global b_entry
    global equation_entry
    global btnEx
    global top2
    global equation_label
    top3 = tk.Toplevel()
    top3.title('Newton Raphson')
    top3.geometry("400x330")
    top3.configure(bg='#3A6F4C')

    # Create equation label and entry
    equation_label = tk.Label(top3, text="Equation:" ,bg='#3A6F4C',fg='#FAAC9A',font=('Helvetica'))
    equation_label.pack(pady=5)             #pack() method is used to organize and display widgets in a container
    equation_entry = tk.Entry(top3)
    equation_entry.pack(pady=2)

    # Create initial guess label and entry
    initial_guess_label = tk.Label(top3, text="Initial Guess:",bg='#3A6F4C',fg='#FAAC9A',font=('Helvetica'))
    initial_guess_label.pack(pady=5)
    initial_guess_entry = tk.Entry(top3)
    initial_guess_entry.pack(pady=2)

    # Create tolerance label and entry
    tolerance_label = tk.Label(top3, text="Tolerance:",bg='#3A6F4C',fg='#FAAC9A',font=('Helvetica'))
    tolerance_label.pack(pady=5)
    tolerance_entry = tk.Entry(top3)
    tolerance_entry.pack(pady=2)

    # Create maximum iterations label and entry
    max_iterations_label = tk.Label(top3, text="Maximum Iterations:",bg='#3A6F4C',fg='#FAAC9A',font=('Helvetica'))
    max_iterations_label.pack(pady=5)
    max_iterations_entry = tk.Entry(top3)
    max_iterations_entry.pack(pady=2)

    # Create the calculate button
    calculate_button = tk.Button(top3, text="Calculate", command=calculateN, bg='#3A6F4C',fg='#FAAC9A',font=('Helvetica'))
    calculate_button.pack(pady=5)

    # Create the result label
    result_label = tk.Label(top3, text="")
    result_label.pack(pady=1)
    
    btnEx = tk.Button(top3, text = 'Exit', command = top3destroy,bg='#3A6F4C',fg='#FAAC9A',font=('S')).pack(pady = 10)
###############################################################################
    
    
    
def topdestroy():
    top.destroy()
    
def top2destroy():
    top2.destroy()
    
def top3destroy():
    top3.destroy()
    
def DesWindow():
    window.destroy()
    
btn = tk.Button(window, text = 'This is Bisection', command = OpenBisection, bg='#a3b18a').grid(row=0, column = 10 , padx = 110, pady = 20)
btn_2 = tk.Button(window, text = 'This is Regula Falsi', command = RegulaExample, bg='#a3b18a').grid(row=1, column = 10 , padx = 110, pady = 20)
btn_2 = tk.Button(window, text = 'This is Newton Raphson', command = NewtonRaphson, bg='#a3b18a').grid(row=2, column = 10 , padx = 110, pady = 20)
btn_3 = tk.Button(window, text = ' Exit ', command = DesWindow, bg='#a3b18a').grid(row=3, column = 10 , padx = 110, pady = 20)

    
# Start the main loop
window.mainloop()

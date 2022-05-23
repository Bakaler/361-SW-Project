from g002_History_Microservice import *
from tkinter import Toplevel, Label, Button, NW
import re
import threading as th
import os


def display_saved_equations(root, calculator):
    """
    Create a new window to display equations saved in f003_List.txt
    """

    # New window object to display saved equations
    newWindow = Toplevel(root)
    newWindow.title("History")
    newWindow.geometry("400x400")

    # Set grid configuration for buttons and equations
    newWindow.columnconfigure(0, weight = 1)
    newWindow.columnconfigure(1, weight = 20)
    for x in range(10):
        newWindow.rowconfigure(x, weight = 1)

    # Populate list w/ equations from f003_List.txt
    equations = get_equations()

    # If there are no equations in file
    if (len(equations)) == 0:
        Label(newWindow,
              text ="There are no equations to display at the moment").grid(row=0, column=0)
        return

    # Display equations in f003_List.txt and a command button for each
    for _ in range(len(equations)):
        Label(newWindow, text = f'{_+1}:  {equations[_]}', font=("Times", 10, "bold")).grid(column=1, row =_, padx=0, pady=4, sticky= NW)
    for _ in range(len(equations)):
        Button(newWindow, width = 5, command = lambda arg1 = _, arg2 = calculator: display_equation(arg1,arg2)).grid(column=0, row=_, padx=0, pady=0, sticky = NW)


def display_equation(lineNumber, calculator):
    equation = parse_equation(lineNumber)

    if not equation:
        return

    calculator.clear_all()
    stat = True
    x = 0

    while x < len(equation):
        stat = calculator.recieve_input(equation[x])
        if stat:
            x += 1
        else:
            calculator.clear_all()

    return


def get_equations():
    """
    Return populated list of saved equations
    """
    with open("f003_List.txt", "r") as f:
        lines = f.readlines()
        f.close()

    return lines


def parse_equation(lineNumber):
    """
    Create populated list of equation to be sent to user_input
    """

    # Allowed user inputs
    functions = {"abs(","sqrt(","neg(","fact(","log(","exp(","square(","recip(","TenPoY("}
    operands = {"+", "-", "*", "**", "/", "%", "//"}

    # Equation in order form (including flattened equations)
    parsedEquation = []

    # TODO MICROSERVICE Retireve Line
    with open("f002_Instruction.txt", "r+") as f:
        f.truncate(0)
        f.write(f"Retrieve {lineNumber}")
        f.close()
    start_microservice()

    while True:
        with open("f001_Data.txt", "r+") as f:
            lines = f.readlines()

            if len(lines) <= 0:
                f.close()
                continue
            line = lines[0].strip('\n')
            f.truncate(0)
            f.close()
            break

    # Parse selected equation
    while line:

        # First value assess
        test = re.match('\S*', line)
        eval_line = line[test.span()[0]: test.span()[1]]

        # End of equation
        if eval_line == "=":
            return parsedEquation

        # Macthes against digits
        elif re.match("^[\d \.]*$", eval_line):
            parsedEquation.append(eval_line)

        # Matches against operands
        elif eval_line in operands:
            parsedEquation.append(eval_line)

        #Matches against functions
        else:
            order = flatten_function(eval_line)
            for _ in order:
                parsedEquation.append(_)

        # Trim equation
        line = line[test.span()[1]+1:]


def flatten_function(line):
    """
    Flatten and return function calls in user inputted order

    :param:
        line - str  :   Function within equation to be flattened

    :return:
        order - list:   Ordered list of user inputs based on equation
    """

    # List to be returned
    order = []

    test = re.match('\w*', line)
    while line:
        # Digit
        if line[test.span()[0]: test.span()[1]].isdigit():
            order.append(line[test.span()[0]: test.span()[1]])
            line = line[test.span()[1]+1:]
        # Function (Or one pretending to be)
        else:
            order.append(line[test.span()[0]: test.span()[1]]+"()")
            line = line[test.span()[1]+1:-1]

        test = re.match('\w*', line)

    # Flip list order
    return order[::-1]

def clear_equation_history():
    """
    Clear all saved equations
    """
    with open("f003_List.txt", "w") as f:
        f.truncate(0)
        f.close()


def save_equation(equation, solution):
    try:
        if equation[-1] == "=":

            with open("f001_Data.txt", "r+") as f:
                f.truncate(0)
                f.write(f'{"{"}"equation": "{equation} {solution}"{"}"}')
                f.close()

            with open("f002_Instruction.txt", "r+") as f:
                f.truncate(0)
                f.write(f"Store")
                f.close()
            start_microservice()


        else:
            print("Invalid")
    except:
        pass




def start_microservice():
    try:
        microThread = th.Thread(target= lambda: os.system("python g002_History_Microservice.py"))
        microThread.start()
    except:
        print("Unable to execute history microservice")
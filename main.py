from tkinter import *
from math import *

root = Tk()
root.geometry("390x415")    #root window size
root.configure(bg = '#e3f0f0')
root.resizable(0,0)         #resize option

root.title("Scientific_Calculator")


class CalculatorWhole():
    '''
    CalculatorWhole class is used to represent as the main function, carrying out all command within the calculator
    '''

    def __init__(self):
        '''
        EL              : Equation Line - Stores the current equations being assessed
        CL              : Command Line - Stores the most up to date command, whether it be equation result or input
        Equations       : All valid scientific calculator equations, holds its own methods
        ValidInputs     : All valid user inputs/button presses
        PreviousInputs  : Stores the previous button pressed for assessment in some cases
        errorStatus     : Reports if an error has been raised to clear everything
        '''
        self._EL = EquationLine()
        self._CL = CommandLine()
        self._Equations = Equations()

        self._validInputs = {"Operands"   : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                             "Operators"  : ['+', '-', '*', '/', '**'],
                             "Solve"      : ["="],
                             "Equations"  : ["1/x", "|x|", "sqrt(x)", "n!", "10^y", "x^2", 'log(n)'],
                             "Special"    : ["CE", "C", "Delete", "π", "+/-", ".", "(", ")"],
                             }
        self._previousInput = None
        self._C_Status = "C"
        self._errorStatus = False

    def set_C(self, status):
        self._C_Status = status

    def get_C(self):
        return self._C_Status

    def solve(self):
        '''
        Assesses the equation held inside the EL and then pushes the integer result to the CL
        '''
        try:
            self._CL.update_value(eval(self._EL.get_Equation()))
        except ZeroDivisionError:
            self._CL.set_command("Error")
            self._errorStatus = True

    def update_equation(self, command_value):
        '''
        :param command_value: Value currently stored within the CL
        Pushes the current value from the CL to the right most side of the EL
        '''
        self._EL.update_Equation(command_value)

    def get_equation(self):
        '''
        returns the current string in the EL
        '''
        return self._EL.get_Equation()

    def clear_equation(self):
        '''
        Clears everything from the EL
        '''
        self._EL.clear_equation()

    def solved_equation(self, solution):
        '''
        After the equation in solved, grabs the integer result from the CL
        I think ?
        #TODO Figure out what this method is doing
        '''
        self._EL.solved_equation(solution)

    def update_command(self, btn_click):
        '''
        Whenever a button is pressed, updates the CL or EL to mimic result of button
        '''

        print(btn_click)
        print("Line     :   Switch Flag     :   Reads")
        print("EL","          " , self._EL.get_switch(), "              " , self.get_equation())
        print("CL","          " , self._CL.get_switch(), "              " , self.get_command())
        print("FR","          ", self._CL.get_functionResult())
        print("Error","       " , self._errorStatus)


        if self._errorStatus == True and btn_click == "=":
            self._CL.clear()
            self._EL.clear_equation()
            self._errorStatus = False
            return

        if self._errorStatus == True:
            self._CL.clear()
            self._EL.clear_equation()
            self._errorStatus = False

        if btn_click in self._validInputs["Operands"]:
            self.operand_command(btn_click)
        elif btn_click in self._validInputs["Operators"]:
            self.operator_command(btn_click)
        elif btn_click in self._validInputs["Solve"]:
            self.solve_command(btn_click)
        elif btn_click in self._validInputs["Equations"]:
            self.equations_command(btn_click)
        elif btn_click in self._validInputs["Special"]:
            self.special_command(btn_click)

        self._previousInput = str(btn_click)

        print()
        print("EL","          " , self._EL.get_switch(), "              " , self.get_equation())
        print("CL","          " , self._CL.get_switch(), "              " , self.get_command())
        print("FR","          ", self._CL.get_functionResult())
        print("Error","       " , self._errorStatus)
        print("---------------------------")

    def operand_command(self, btn_click):
        # '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

        if self._CL.get_functionResult() == True:
            self._CL.set_functionResult()

        if self._EL.get_switch() == True:
            self._EL.set_switch(False)
            self._EL.clear_equation()

            if self._CL.get_switch() == True:
                self._CL.set_command(btn_click)
                self._CL.set_switch(False)

            else:
                self._CL.update_value(btn_click)

        elif self._previousInput == ")":
            if len(str(self._EL.get_Equation())) == 0:
                self._CL.set_command(btn_click)
                return

            elif self._CL.get_switch() == True:
                self._CL.set_switch(False)
                self._CL.set_command(btn_click)
            temp_store = str(self._EL.get_Equation())
            index = -1

            while temp_store[index] != "(":
                index -= 1
                if abs(index) == len(temp_store):
                    break

            temp_store = self._EL.get_Equation()[:index]
            self._EL.clear_equation()
            self._EL.update_Equation(temp_store)

        elif self._CL.get_switch() == True:
            if self._previousInput in self._validInputs["Equations"]:
                temp_index = -1
                temp_equation = self._EL.get_Equation()

                if len(temp_equation) != 0:
                    while temp_equation[temp_index] != " ":
                        temp_index -= 1
                        if abs(temp_index) == len(temp_equation):
                            break

                    self._EL.clear_equation()
                    self._EL.update_Equation(temp_equation[:temp_index])

                    self._EL.set_switch(True)
            self._CL.set_command(btn_click)
            self._CL.set_switch(False)

        elif len(self._CL.get_command()) >= 19:
            return

        else:
            if self._previousInput in self._validInputs["Equations"]:
                self._EL.set_switch(True)
                self._CL.set_command(btn_click)
            else:
                self._CL.update_value(btn_click)

    def operator_command(self, btn_click):
        # '+', '-', '*', '/', **

        if self._previousInput == "**":
            pass

        elif self._previousInput == ")":
            self._EL.update_Equation(" " + btn_click + " ")

        elif self._previousInput == "(":
            self._EL.update_Equation(self._CL.get_command() + " " + btn_click + " ")
            self._CL.set_switch(True)

        elif self._previousInput in self._validInputs["Operators"]:
            temp_equation = self.get_equation()
            temp_equation = temp_equation[0:-3]
            self._EL.clear_equation()
            self._EL.update_Equation(temp_equation)
            self._EL.update_Equation(" " + btn_click + " ")

        elif self._EL.get_switch() == True:
            self._EL.set_switch(False)

            self._EL.solved_equation(self._CL.get_command())
            self._EL.update_Equation(" " + btn_click + " ")

            # If previous input was an Equation, CL does not get over written
            if self._previousInput in self._validInputs["Equations"]:
                self._CL.set_switch(False)
            # If previous input was else, over writes
            else:
                self._CL.set_switch(True)

        elif len(self._EL.get_Equation()) != 0 and self._previousInput in self._validInputs["Operands"] and \
             self._EL.get_Equation()[-1] != " ":
                self._EL.update_Equation(self.get_command())
                self._EL.update_Equation(" " + btn_click + " ")
                self._CL.set_switch(True)


        elif self._previousInput in self._validInputs["Equations"]:
            if len(self._EL.get_Equation()) == 0:
                self._EL.update_Equation(self._CL.get_command())
            self._EL.update_Equation(" " + btn_click + " ")
            self._CL.set_switch(True)


        elif self._CL.get_functionResult() == True:
            self._CL.set_functionResult()
            self._EL.update_Equation(" " + btn_click + " ")
            self._CL.set_switch(True)

            # In the case we want to push the CL to the EL
        else:
            self._EL.update_Equation(self.get_command())
            self._EL.update_Equation(" " + btn_click + " ")
            self._CL.set_switch(True)

    def equations_command(self, btn_click):
        # "1/x", "|x|", "sqrt(x)", "n!", "10^y", "x^2"
        if self.equation_checker(btn_click) is False:
            return

        if "-" in str(self._CL.get_command()):
            temp_store = str(self._CL.get_command())
            self._CL.set_command(str("("+ temp_store + ")"))

        if self._previousInput == ")":
            if len(self._EL.get_Equation()) != 0:
                temp_store = str(self._EL.get_Equation())
                index = -1
                while temp_store[index] != "(":
                    index -= 1
                    if abs(index) == len(temp_store):
                        break

                index -= 1
                temp_store = self._EL.get_Equation()[:index]
                self._EL.clear_equation()
                self._EL.update_Equation(temp_store)

        if self._EL.get_switch() == True:
            self._EL.set_switch(False)
            temp_store = self._Equations.get_and_return_equation(btn_click, self.get_command())
            # Integer Value (such that 1/100 = .01)
            value = eval(temp_store)
            # Str of function (such that 1/x = 1/100)
            str_val = "(" + temp_store + ")"

            self._CL.set_functionResult()
            self._EL.solved_equation(str_val)
            self._CL.set_command(value)

        elif self._previousInput in self._validInputs["Equations"]:


            if self.get_equation() != "":
                temp_store = self._Equations.get_and_return_equation(btn_click, self.get_equation())

            else:
                temp_store = self._Equations.get_and_return_equation(btn_click, "0")

            self._EL.clear_equation()
            # Integer Value (such that 1/100 = .01)

            try:
                value = eval(temp_store)
            except OverflowError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return
            except ZeroDivisionError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return
            except ValueError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return
            # Str of function (such that 1/x = 1/100)
            str_val = "(" + temp_store + ")"

            self._CL.set_functionResult()
            self._EL.update_Equation(str_val)
            self._CL.set_command(value)
            self._CL.set_switch(True)

        else:
            temp_store = self._Equations.get_and_return_equation(btn_click, self.get_command())

            # Integer Value (such that 1/100 = .01)
            try:
                value = eval(temp_store)
            except OverflowError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return
            except ZeroDivisionError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return
            # Str of function (such that 1/x = 1/100)
            str_val = "(" + temp_store + ")"

            self._CL.set_functionResult()
            self._EL.update_Equation(str_val)
            count = self.paran_count()
            while count != 0:
                self._EL.update_Equation(")")
                count -= 1
            self._CL.set_command(value)
            self._CL.set_switch(True)

    def equation_checker(self, function_input):
        if function_input == "1/x":
            pass
        if function_input == "|x|":
            if float(self._CL.get_command()) > 999999999999999999999999999:
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
            else:
                return True
        if function_input == "sqrt(x)":
            pass
        if function_input == "n!":
            if not (float(self.get_command())).is_integer():
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
            elif float(self._CL.get_command()) > 25:
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
            elif float(self._CL.get_command()) < 0:
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
            else:
                return True
        if function_input == "log(n)":
            if float(self._CL.get_command()) <= 0:
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
        if function_input == "10^y":
            if float(self._CL.get_command()) > 23:
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
            else:
                return True
        if function_input == "x^2":
            if float(self._CL.get_command()) > 9999999999999:
                self._CL.set_command("Error")
                self._errorStatus = True
                return False
            else:
                return True

    def special_command(self, btn_click):
        # "CE", "C", "Delete", "π", "+/-", ".", "(", ")"
        # CE & C
        # When CL blank at default, "C"
        # Sets CL to "0"/ Clears
        # When CL has a value
        # When EL blank at default, "CE"
        # Sets CL to "0" / Clears
        # When CL has a value
        # When EL is storing an equations, "CE"
        # Sets CL to "0"/ Clears
        # EL stays intact

        # When do these get set??
        # When a value is passed to the CL
        # C turns to CE

        # What is talking to what here?
        # Btn_click = 8
        # Because 8 exist within the CL, what is
        # telling the buttons to switch?

        if btn_click == "C":
            self.clear_equation()
        elif btn_click == "CE":
            if self.get_command() != "0" and len(self.get_equation()) != 0 and (self.get_equation()[-1] == "=" or
                                self._previousInput in self._validInputs["Equations"] ):
                self.clear_equation()
                self._EL.set_switch(False)
            elif self.get_command() == "0" and len(self.get_equation()) != 0:
                self.clear_equation()
                self._EL.set_switch(False)
            elif self._previousInput in self._validInputs["Equations"]:
                try:
                    location = len(self._EL.get_Equation()) -1
                    while self._EL.get_Equation()[location] != " ":
                        location -= 1
                    temp = self._EL.get_Equation()[0:location]
                    self._EL.clear_equation()
                    self._EL.update_Equation(temp)
                except IndexError:
                    pass
            self._CL.set_switch(False)
            self.clear_command()

            if self._CL.get_functionResult() == True:
                self._CL.set_functionResult()

        elif btn_click == "Delete":
            self._CL.set_command(str(self.get_command())[0:-1])
            if self._CL.get_command() == "":
                self._CL.set_command("0")
        elif btn_click == "π":
            self._CL.set_command('3.1415926535')
            self._CL.set_switch(True)
            self._EL.set_switch(True)
        elif btn_click == "+/-":
            if self._previousInput in self._validInputs["Equations"]:
                self._EL.set_switch(True)

            if self._CL.get_command() != 0 and self._CL.get_command() != "":
                temp_string = self._CL.get_command()
                print("value", temp_string)
                if float(temp_string) > 0:
                    self._CL.set_command("-" + str(temp_string))
                elif float(temp_string) < 0:
                    temp_string = str(temp_string[1:])
                    self._CL.set_command(temp_string)
        elif btn_click == ".":
            if self._CL.get_switch() == True:
                self._CL.set_switch(False)
                self._CL.clear()
                self._CL.update_value(btn_click)

            elif str(self.get_command())[-1] != ".":
                self._CL.update_value(btn_click)
        elif btn_click == "(":
            if len(self._EL.get_Equation()) != 0:
                if self._EL.get_Equation()[-1] == ")":
                    return
            if self._EL.get_switch() == True or self._previousInput in self._validInputs["Equations"]:
                self._EL.clear_equation()
                self._EL.set_switch(False)
            self._EL.update_Equation(btn_click)
        elif btn_click == ")":
            count = self.paran_count()
            if count > 0:
                print("Bingo")
                # print("((")
                if self._previousInput == "(" and self._CL.get_command() == "0":
                    self._EL.update_Equation("0")
                else:
                    self._EL.update_Equation(self._CL.get_command())
                self._EL.update_Equation(btn_click)
                self._CL.set_switch(True)

    def solve_command(self, btn_click):
        # "="

        # Used to solve the equation
        # Takes the String of the EL, evaluates it, and pushes result to the CL
        # EL switch will = True
        # CL switch will = True
        if self._CL.get_command() == "Error":
            return

        if self._previousInput in self._validInputs["Equations"] and self._EL.get_Equation() != "":
            self._CL.set_command(eval(self._EL.get_Equation()))
            self._EL.update_Equation(" " + btn_click)
            self._EL.set_switch(True)
            self._CL.set_switch(True)

        elif self._previousInput == "=":
            # In the case "=" is pressed consecutively
            equation = self._EL.get_Equation()
            x = 0
            while str.isspace(equation[x]) is not True:
                x += 1

            new_equation = str(self._CL.get_command()) + " " + str(self._EL.get_Equation()[x+1:-2])
            self._EL.clear_equation()
            self._EL.update_Equation(new_equation)

            count = self.paran_count()
            while count != 0:
                self._EL.update_Equation_front()
                count += 1

            try:
                solved_equation = eval(self._EL.get_Equation())
                if len(str(solved_equation)) > 27:
                    self._CL.set_command("Error")
                    self._errorStatus = True
                    return
                else:
                    self._CL.set_command(solved_equation)
            except ZeroDivisionError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return

            self._EL.update_Equation(" " + btn_click)
            self._EL.set_switch(True)
            self._CL.set_switch(True)
        else:
            if self._previousInput != ")":
                self._EL.update_Equation(self.get_command())
            count = self.paran_count()
            while count != 0:
                self._EL.update_Equation(")")
                count -= 1

            try:
                if "=" in self._EL.get_Equation():
                    temp = str(self._EL.get_Equation())
                    temp = temp[0:-2]
                    self._CL.clear()
                    self._EL.clear_equation()
                    self._EL.update_Equation(temp)
                    #TODO Just going to live with that space ATM

                solved_equation = eval(self._EL.get_Equation())
                if len(str(solved_equation)) > 27:
                    self._CL.set_command("Error")
                    self._errorStatus = True
                    return
                else:
                    self._CL.set_command(solved_equation)
            except ZeroDivisionError:
                self._CL.set_command("Error")
                self._errorStatus = True
                return

            self._EL.update_Equation(" " + btn_click)
            self._EL.set_switch(True)
            self._CL.set_switch(True)

    def clear_command(self):
        '''
        :return: Clears the CL
        '''
        self._CL.clear()

    def get_command(self):
        '''
        :return: CL integer
        '''
        return self._CL.get_command()

    def displayCalc(self):
        '''
        Used for debugging
        '''
        print("Equation Line :", self.get_equation())
        print("Command Line  :", self.get_command())

    def displaySwitches(self):
        '''
        Used for debugging
        '''
        print("Equation Switch  :", self._EL.get_switch())
        print("Command Switch   :", self._CL.get_switch())

    def paran_count(self):
        '''
        Count -
            Positive indicates more "(" in an equation
            Negative indicates more ")" in an equation
            0 indicates even amount
        :return: Count value of parans in an equation
        '''
        count = 0

        # Iterates through the equation, investigating each character
        for value in str(self._EL.get_Equation()):
            # For opened
            if value == "(":
                count += 1
            # For closed
            elif value == ")":
                count -= 1

        return count

class EquationLine():
    '''
    Top most line within the Sci-Cal that stores the most current equation
    Ultimately used to assess all equations inputted by user
    #TODO Find max length
    '''

    def __init__(self):
        '''
        Equation is stored as a string
            '1 + 1/100 + 8'
        newEquation is used whenever the user presses "=" indicating to clear and update the Equation string
        '''
        self._equation = ""
        self._newEquation = False
        self._ELDisplay = Equation_Line()

    def get_Equation(self):
        '''
        :return: EL string
        '''
        return self._equation

    def update_Equation(self, value):
        '''
        :param value: integer value from CL to be pushed
        :return: Adds the CL integer to the right most of the EL string
        '''
        if "-" in value and " " not in value:
            self._equation += str("("+ str(value)+ ")")
        else:
            self._equation += str(value)
        self._ELDisplay.set_equationLine(self._equation)

    def update_Equation_front(self):
        self._equation = self._equation[:0] + "(" + self._equation[0:]

    def clear_equation(self):
        '''
        :return: Resets the EL to a blank state
        '''
        self._equation = ""
        self._ELDisplay.set_equationLine(self._equation)

    def solved_equation(self, solution):
        """
        When an equation is solved, used to update the EL whenever a function is used
        Such that 9 * 9 = 81
        Sqrt(x)
        EL = sqrt(81)
        """
        self._equation = str(solution)
        self._ELDisplay.set_equationLine(self._equation)

    def set_switch(self, Boolean):
        '''
        :return: Sets newEquation to True or False
        '''
        self._newEquation = Boolean

    def get_switch(self):
        '''
        returns True or False, depending on EL clear
        '''
        return self._newEquation


class CommandLine():
    '''
    User inputted integers that are pushed into the EL for assessment
    '''

    def __init__(self):
        '''
        command - String used to store 'integer' inside the CL
        newCommand Sets to clear the Command Line for a new value
        functionResult
                A function was inputted, so a value doesn't need to be
                pushed to the Command Line
        '''
        self._command = "0"
        self._newCommand = False
        self._functionResult = False
        self._CLDisplay = Command_Line()

    def get_functionResult(self):
        '''
        :return: True or False, based on functionResult
        '''
        return self._functionResult

    def set_functionResult(self):
        '''
        Sets the function result to the opposite value
        '''
        if self._functionResult == False:
            self._functionResult = True
        else:
            self._functionResult = False

    def clear(self):
        '''
        Reverts the CL to an empty string
        '''
        self._command = "0"
        self._CLDisplay.set_commandLine(self._command)

    def update_value(self, btn_click):
        '''
        updates the CL integer
        '''

        if self._command == "0":
            if btn_click == ".":
                self._command = "0."
            else:
                self._command = btn_click
        else:
            if btn_click == "." and "." not in self.get_command():
                self._command += btn_click
            elif btn_click != ".":
                self._command += btn_click
        try:
            if (float(self.get_command())).is_integer():
                self.set_command(int(self.get_command()))
                self.set_command(str(self.get_command()))

        except ValueError:
            pass

        self._CLDisplay.set_commandLine(self._command)
        # 1 is in the CL, user presses '2'
        # (1 * 10) + 2 = 12
        # CL reads 12

    def set_command(self, btn_click):
        '''
        ?
        '''
        if btn_click == ".":
            self._command = "0."
        else:
            self._command = btn_click
            try:
                if (float(self.get_command())).is_integer():
                    self._command = int(self.get_command())
                    self._command = str(self.get_command())
            except ValueError:
                self._command = str(self.get_command())

        self._CLDisplay.set_commandLine(self._command)

    def get_command(self):
        '''
        :return: Integer value stored in the CL
        '''
        return self._command

    def set_switch(self, Boolean):
        '''
        Sets the CL switch to True or False
        '''
        self._newCommand = Boolean

    def get_switch(self):
        '''
        :return: True or False
        '''
        return self._newCommand

class Equations():

    def get_and_return_equation(self, function_input, command_input):
        if function_input == "1/x":
            return self.mul_inv(command_input)
        if function_input == "|x|":
            return self.absolute(command_input)
        if function_input == "sqrt(x)":
            return self.sqrt(command_input)
        if function_input == "n!":
            return self.fact(command_input)
        if function_input == "log(n)":
            return self.logarithmic(command_input)
        if function_input == "10^y":
            return self.fact10(command_input)
        if function_input == "x^2":
            return self.square(command_input)

    # multiplicative inverse (1/x)
    def mul_inv(self, x):

        return "1/" + str(x)

    #Absolute Value
    def absolute(self, x):

        return "abs(" + str(x) + ")"

    # Square Root
    def sqrt(self, x):

        return "sqrt(" +str(x) + ")"

    # Factorial
    def fact(self, x):

        return "factorial(" + str(x) + ")"

    # Logarithmic
    def logarithmic(self, x):

        return "log(" + str(x) + ",10)"

    def fact10(self, x):
        return "(10 ** " + str(x) + ")"

    def square(self, x):

        return "(" + str(x) + "**2)"

#-----------------------------------
#USER INTERFACE
#-----------------------------------

class Displays():

    def __init__(self):
        self._button_display = Button_Display()

class Button_Display():

    def __init__(self):
        self._colorMain = "#b5b3c2"
        self._colorOff = "#ceccd9"
        self._btns_frame = Frame(root, width=390, height=300, bg="grey")
        self._btns_frame.pack(side = BOTTOM)

        # TODO Do i communicate to the CL and EL through the CalcWhole?
            # I don' think I should, but just in case ^^
            # Button -> Calc -> CL
        self._Calc = CalculatorWhole()
        self._clear = StringVar()
        self._clear.set("C")
        self._buttons = self.Buttons()

    def Buttons(self):
        self._b1 = Button(self._btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "π")).grid(row = 0, column = 0, padx = 1, pady = 1)

        self._b2 = Button(self._btns_frame, text = "1/x", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self._Calc.update_command(
                        "1/x")).grid(row = 0, column = 1, padx = 1, pady = 1)

        self._b3 = Button(self._btns_frame, text = "|x|", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self._Calc.update_command(
                        "|x|")).grid(row = 0, column = 2, padx = 1, pady = 1)

        # Special Cases, button switches between C and CE


        self._b4 = Button(self._btns_frame, text="C", fg="black", width=10, height=3, bd=0,
                        bg=self.get_colorOff(), cursor="hand2", command=lambda: self.send_commands(
                        "C")).grid(row=0, column=3, padx=1, pady=1)

        self._b5 = Button(self._btns_frame, text = "Delete", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._Calc.update_command(
                        "Delete")).grid(row = 0, column = 4, padx = 1, pady = 1)

        # Row 2
        self._b6 = Button(self._btns_frame, text = "Sqrt(x)", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "sqrt(x)")).grid(row = 1, column = 0, padx = 1, pady = 1)

        self._b7 = Button(self._btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "(")).grid(row = 1, column = 1, padx = 1, pady = 1)

        self._b8 = Button(self._btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        ")")).grid(row = 1, column = 2, padx = 1, pady = 1)

        self._b9 = Button(self._btns_frame, text = "n!", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "n!")).grid(row = 1, column = 3, padx = 1, pady = 1)

        self._b10 = Button(self._btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "/")).grid(row = 1, column = 4, padx = 1, pady = 1)

        # Row 3
        self._b11 = Button(self._btns_frame, text = "x^y", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "**")).grid(row = 2,  column = 0, padx = 1, pady = 1)

        self._b12 = Button(self._btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "7")).grid(row = 2, column = 1, padx = 1, pady = 1)

        self._b13 = Button(self._btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "8")).grid(row = 2, column = 2, padx = 1, pady = 1)

        self._b14 = Button(self._btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "9")).grid(row = 2, column = 3, padx = 1, pady = 1)

        self._b15 = Button(self._btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "*")).grid(row = 2, column = 4, padx = 1, pady = 1)

        # Row 4
        self._b16 = Button(self._btns_frame, text = "10^y", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "10^y")).grid(row = 3,column = 0, padx = 1, pady = 1)

        self._b17 = Button(self._btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "4")).grid(row = 3,  column = 1, padx = 1, pady = 1)

        self._b18 = Button(self._btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "5")).grid(row = 3, column = 2, padx = 1, pady = 1)

        self._b19 = Button(self._btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "6")).grid(row = 3, column = 3, padx = 1, pady = 1)

        self._b20 = Button(self._btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "-")).grid(row = 3, column = 4, padx = 1, pady = 1)

        # Row 5
        self._b21 = Button(self._btns_frame, text = "log(n)", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "log(n)")).grid(row = 4, column = 0, padx = 1, pady = 1)

        self._b22 = Button(self._btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "1")).grid(row = 4,  column = 1, padx = 1, pady = 1)

        self._b23 = Button(self._btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "2")).grid(row = 4, column = 2, padx = 1, pady = 1)

        self._b24 = Button(self._btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "3")).grid(row = 4, column = 3, padx = 1, pady = 1)

        self._b25 = Button(self._btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "+")).grid(row = 4, column = 4, padx = 1, pady = 1)

        # Row 6
        self._b26 = Button(self._btns_frame, text = "x^2", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "x^2")).grid(row = 5, column = 0, padx = 1, pady = 1)

        #TODO Figure out how were going to implement sign changes
        self._b27 = Button(self._btns_frame, text = "+/-", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_color(), cursor = "hand2", command = lambda: self.send_commands(
                        "+/-")).grid(row = 5, column = 1, padx = 1, pady = 1)

        self._b28 = Button(self._btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "0")).grid(row = 5, column = 2, padx = 1, pady = 1)

        self._b29 = Button(self._btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        ".")).grid(row = 5, column = 3, padx = 1, pady = 1)

        self._b30 = Button(self._btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self.send_commands(
                        "=")).grid(row = 5, column = 4, padx = 1, pady = 1)

    def get_color(self):
        return self._colorMain

    def get_colorOff(self):
        return self._colorOff

    def get_btns_frame(self):
        return self._btns_frame

    def get_clear(self):
        return self._clear

    def send_commands(self, x):
        self._Calc.update_command(x)
        self.set_clear_status()


    def set_clear_status(self):
        if self._Calc.get_command() == "0" and len(self._Calc.get_equation()) == 0:
            self._clear = "C"
        else:
            self._clear = "CE"

        self._b4 = Button(self._btns_frame, text=self.get_clear(), fg="black", width=10, height=3, bd=0,
                    bg=self.get_color(), cursor="hand2", command=lambda: self.send_commands(
                    str(self.get_clear()))).grid(row=0, column=3, padx=1, pady=1)


class Command_Line():

    def __init__(self):
        self._expression = ""
        self._commandLine = StringVar()
        self.set_commandLine("0")

        self._input_frame = Frame(root, width=312, height=50, bg = '#e3f0f0')
        self._input_frame.pack(side=TOP, padx = 10)

        self._input_field = Entry(self._input_frame, font=('ariel', 18, 'bold'),
                                  textvariable=self.get_commandLine(),
                                  width=50, bg='#e3f0f0', bd=0, justify=RIGHT)
        self._input_field.grid(row=0, column=0)
        self._input_field.pack(ipady=5)  # ipady is internal padding that increases the height of the input field

    def get_input_frame(self):
        return self._input_frame


    def get_commandLine(self):
        return self._commandLine

    def set_commandLine(self, expression):
        self._commandLine.set(expression)
        return self._commandLine

    def btn_click(self, item):
        self._expression += str(item)
        self._commandLine.set(expression)

class Equation_Line():

    def __init__(self):
        self._expression = ""
        self._equationLine = StringVar()
        self._pass_frame = Frame(root, width=390, height=25, bd=0)
        self._pass_frame.pack(side=TOP)

        self._pass_field = Label(self._pass_frame, font=('ariel', 10), textvariable=self._equationLine, width=50,
                                 bg='#829f9f',
                           bd=0, anchor="e")
        self._pass_field.grid(row=0, column=0)
        self._pass_field.pack(ipady=10)

    def display_equation(self):
        #TODO Figure out how to pass it up to field
        pass

    def get_equationLine(self):
        return self._equationLine

    def set_equationLine(self, expression):
        self._equationLine.set(expression)
        return self._equationLine


    def add_to_equation(self, item):
        self._expression += str(item)
        self._equationLine.set(expression)



class Functions:

    def __init__(self):
        self._text = StringVar()

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text.set(text)
        return self._text

    def btn_click(self, item):
        '''
        btn_function updates the input field whenever a number is entered
        param item:
        :return:
        '''
        global expression
        expression = expression + str(item)
        self._text.set(expression)


program = Frame(root)
program.pack()
lf = Displays()
root.mainloop()
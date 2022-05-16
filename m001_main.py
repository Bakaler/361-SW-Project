# Tkinter import from
# m002, m003,

from math import *

from m002_ELD import *
from m003_CLD import *
from m004_EL import *
from m005_CL import *
from m006_Equation import *
from m007_EBNF import *
from m008_ButtonDisplay import *



class Calculator():

    def __init__(self, root):
        self._functionMap = {
            "abs()"     :   ["abs(.*)", "abs("],
            "sqrt()"    :   ["sqrt(.*)", "sqrt("],
            "neg()"     :   ["neg(.*)", "neg("],
            "fact()"    :   ["fact(.*)", "fact("],
            "log()"     :   ["log(.*)", "log("],     #TODO Base
            "exp()"     :   ["exp(.*)", "exp("],
            "square()"  :   ["square(.*)", "square("],
            "recip()"   :   ["recip(.*)", "recip("],  #TODO Special implementation
            "TenPoY()"  :   ["TenPoY(.*)", "TenPoY("] #TODO Special implementation
        }


        self._ELDisplay = ELDisplay(root)
        self._CLDisplay = CLDisplay(root)
        self._buttonDisplay = ButtonDisplay(root, self)

        self._equationLine = EquationLine(self._ELDisplay)
        self._commandLine = CommandLine(self._CLDisplay)
        self._Equation = Equation()

        self._parser = EBNF_parser(self._functionMap)


    def get_equation_line(self) -> str:
        return self._equationLine.get_equation_line()


    def set_equation_line(self, equation : str) -> None:
        self._equationLine.set_equation_line(equation)


    def get_command_line(self) -> str:
        return self._commandLine.get_command_line()


    def set_command_line(self, command : str) -> None:
        self._commandLine.set_command_line(command)

    def recieve_input(self, userInput : str) -> None:
        self.pass_to_parser(userInput, self.get_equation_line(), self.get_command_line())


    def pass_to_parser(self, userInput : str, equationLine : str, commandLine : str):
        """
        Recieve, validate, and execute user input

        :params:
            userInput       - User userInput
            equationLine    - Equation line
            commandLine     - Command line
        :returns:
            None
        """

        # (bool, EL, CL)
        result = self._parser.parse(userInput, equationLine, commandLine)

        # if result was invalid, return from parsing
        if not result[0]:
            return

        # Update userInput & equation line classes // gui
        self.set_equation_line(result[1])
        self.set_command_line(result[2])

    def clear_entry(self):
        self.set_command_line("0")

    def clear_all(self):
        self.set_equation_line("")
        self.set_command_line("0")


if __name__ == "__main__":
    root = Tk()
    root.geometry("390x415")    #root window size
    root.configure(bg = '#e3f0f0')
    root.resizable(0,0)         #resize option

    root.title("Scientific & Graphing Calculator")

    program = Frame(root)
    program.pack()

    Calculator(root)

    root.mainloop()
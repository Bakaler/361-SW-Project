# Tkinter import from
# m002, m003,

from math import *

from m002_ELD import *
from m003_CLD import *
from m004_EL import *
from m005_CL import *
from m006_EBNF import *
from m007_ButtonDisplay import *
from m008_Menu import *



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

        #GUIs

        self._ELDisplay = ELDisplay(root)
        self._CLDisplay = CLDisplay(root)
        self._buttonDisplay = ButtonDisplay(root, self)
        self._Menu = MenuDisplay(root, self, self._ELDisplay, self._CLDisplay, self._buttonDisplay)

        # Logic Centers
        self._equationLine = EquationLine(self._ELDisplay)
        self._commandLine = CommandLine(self._CLDisplay)

        #EBNF/Parser
        self._parser = EBNF_parser(self._functionMap)


    def get_equation_line(self) -> str:
        """
        Get equation line string from Equation Line object
        """
        return self._equationLine.get_equation_line()


    def set_equation_line(self, equation : str) -> None:
        """
        Set equation line string inside Equation Line object
        """
        self._equationLine.set_equation_line(equation)


    def get_command_line(self) -> str:
        """
        Get command line string from Command Line object
        """
        return self._commandLine.get_command_line()


    def set_command_line(self, command : str) -> None:
        """
        Set command line string inside Command Line object
        """
        self._commandLine.set_command_line(command)


    def recieve_input(self, userInput : str) -> bool:
        """
        Get input from user and send to parser

        return:
            True    :   If input is valid
            False   :   If input is invalid
        """
        # (bool, Equation Line : str, Command Line : str)
        result = self._parser.parse(userInput, self.get_equation_line(), self.get_command_line())

        # if result was invalid, return from parsing
        if not result[0]:
            return False

        # Update userInput & equation line classes // gui
        self.set_equation_line(result[1])
        self.set_command_line(result[2])

        return True


    def clear_entry(self):
        """
        Clear command line and set to 0
        """
        self.set_command_line("0")


    def clear_all(self):
        """
        Clear equation line and set command line to 0
        """
        self.set_equation_line("")
        self.set_command_line("0")


if __name__ == "__main__":

    # Tkinter GUI main set-up
    root = Tk()
    root.geometry("390x405")
    root.configure(bg = '#000000')
    root.resizable(0,0)

    root.title("Scientific & Graphing Calculator")

    program = Frame(root)
    program.pack()

    Calculator(root)

    root.mainloop()
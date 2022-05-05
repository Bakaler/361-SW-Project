# Tkinter import from
# m002, m003, 

from math import *

from m002_ELD import *
from m003_CLD import *
from m004_EL import *
from m005_CL import *
from m006_Equation import *
from m007_LogicUnit import *
from m008_ScientificDisplay import *



class Initialization():

    def __init__(self, root):
        self._ELDisplay = ELDisplay(root)
        self._CLDisplay = CLDisplay(root)

        self._EquationLine = EquationLine(self._ELDisplay)
        self._CommandLine = CommandLine(self._CLDisplay)
        self._Equation = Equation()

        self._LogicUnit = LogicUnit(self._EquationLine, self._CommandLine, self._Equation)

        self._ScientificDisplay = ScientificDisplay(self._LogicUnit)


if __name__ == "__main__":
    root = Tk()
    root.geometry("390x415")    #root window size
    root.configure(bg = '#e3f0f0')
    root.resizable(0,0)         #resize option

    root.title("Scientific & Graphing Calculator")

    program = Frame(root)
    program.pack()

    Initialization(root)

    root.mainloop()
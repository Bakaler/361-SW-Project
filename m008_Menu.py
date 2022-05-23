from tkinter import *
from g003_History_Functions import *

class MenuDisplay:

    def __init__(self, root, calculator):
        self._calculator = calculator

        self._menu = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
        root.config(menu=self._menu)
        self._history = self.create_history_window(root)


    def create_history_window(self, root):
        history = Menu(self._menu, tearoff=0, background='#ffcc99', foreground='black')
        history.add_command(label = "Save Equation", command =  lambda arg1 = self._calculator: save_equation(arg1.get_equation_line(), arg1.get_command_line()))
        history.add_command(label = "View History", command = lambda arg1 = root, arg2 = self._calculator: display_saved_equations(arg1, arg2)) # display_saved_equations
        history.add_separator()
        history.add_command(label = "Clear History", command= clear_equation_history) # clear_equation_history
        self._menu.add_cascade(label = "History", menu=history)
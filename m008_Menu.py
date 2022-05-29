from tkinter import *
from g003_History_Functions import *
from g002_Color_Themes import *

class MenuDisplay:

    def __init__(self, root, calculator, CLD, ELD, Buttons):
        self._calculator = calculator

        self._menu = Menu(root, background='#ceccd9', foreground='black', activebackground='white', activeforeground='black')
        root.config(menu=self._menu)
        self._history = self.create_history_window(root)
        self._colors = self.create_color_themes(CLD, ELD, Buttons)


    def create_history_window(self, root):
        history = Menu(self._menu, tearoff=0, background='#ceccd9', foreground='black')
        history.add_command(label = "Save Equation", command =  lambda arg1 = self._calculator: save_equation(arg1.get_equation_line(), arg1.get_command_line()))
        history.add_command(label = "View History", command = lambda arg1 = root, arg2 = self._calculator: display_saved_equations(arg1, arg2)) # display_saved_equations
        history.add_separator()
        history.add_command(label = "Clear History", command= clear_equation_history) # clear_equation_history
        self._menu.add_cascade(label = "History", menu=history)

    def create_color_themes(self, CLD, ELD, Buttons):
        colors = Menu(self._menu, tearoff=0, foreground='black')
        colors.add_command(label = "Default", command = lambda arg0 = "1", arg1 = CLD, arg2 = ELD, arg3 = Buttons:
                            set_theme(arg0, arg1, arg2, arg3), background='#b5b3c2')
        colors.add_command(label = "Boot", command = lambda arg0 = "2", arg1 = CLD, arg2 = ELD, arg3 = Buttons:
                            set_theme(arg0, arg1, arg2, arg3), background='#52796f')
        colors.add_command(label = "Starburst", command = lambda arg0 = "3", arg1 = CLD, arg2 = ELD, arg3 = Buttons:
                            set_theme(arg0, arg1, arg2, arg3), background='#fcb9b2')
        colors.add_command(label = "Amphibian", command = lambda arg0 = "4", arg1 = CLD, arg2 = ELD, arg3 = Buttons:
                            set_theme(arg0, arg1, arg2, arg3), background='#99d98c')
        colors.add_command(label = "SoCal", command = lambda arg0 = "5", arg1 = CLD, arg2 = ELD, arg3 = Buttons:
                            set_theme(arg0, arg1, arg2, arg3), background='#00afb9')
        self._menu.add_cascade(label = "Themes", menu=colors)
from tkinter import *

class ELDisplay:

    def __init__(self, root):
        self._expression = ""
        self._equationLine = StringVar()
        self._pass_frame = Frame(root, width=390, height=25, bd=0)
        self._pass_frame.pack(side=TOP)

        self._pass_field = Label(self._pass_frame, font=('ariel', 10), textvariable=self._equationLine, width=50,
                                 bg='#829f9f',
                           bd=0, anchor="e")
        self._pass_field.grid(row=0, column=0)
        self._pass_field.pack(ipady=10)

    def get_equationLine(self):
        return self._equationLine

    def set_equationLine(self, expression):
        self._equationLine.set(expression)
        return self._equationLine

    #TODO Removed
    """
    def add_to_equation(self, item):
        self._expression += str(item)
        self._equationLine.set(expression)
    """
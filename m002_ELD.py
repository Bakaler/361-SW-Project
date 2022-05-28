from tkinter import *

class ELDisplay:
    """
    GUI front face to display equation line

    Stores equation string
    """

    def __init__(self, root):
        self._equationLine = StringVar()

        self._equation_frame = Frame(root, width=390, height=25, bd=0)
        self._equation_frame.pack(side=TOP)

        self._equation_field = Label(self._equation_frame, font=('ariel', 10),
                                    textvariable=self._equationLine, width=50,
                                    bg='#829f9f', bd=0, anchor="e")
        self._equation_field.grid(row=0, column=0)
        self._equation_field.pack(ipady=10)

    def get_equation_line(self):
        """
        Return current equation line
        """
        return self._equationLine

    def set_equation_line(self, expression : str) -> str:
        """
        Update / Set equation line
        """
        self._equationLine.set(expression)
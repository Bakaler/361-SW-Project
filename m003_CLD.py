from tkinter import *

class CLDisplay:

    def __init__(self, root):
        self._expression = ""
        self._commandLine = StringVar()
        self.set_commandLine("0")

        self._input_frame = Frame(root, width=312, height=50, bg = '#e3f0f0')
        self._input_frame.pack(side=TOP, padx = 10)

        self._input_field = Entry(self._input_frame, font=('ariel', 18, 'bold'),
                                  textvariable=self.get_commandLine(),
                                  width=50, bg='#e3f0f0', bd=0, justify=RIGHT)
        self._input_field.grid(row=0, column=0)
        self._input_field.pack(ipady=5)

    def get_commandLine(self):
        return self._commandLine

    def set_commandLine(self, expression):
        self._commandLine.set(expression)
        return self._commandLine

    # TODO Removed
    """
    def btn_click(self, item):
        self._expression += str(item)
        self._commandLine.set(expression)
    """

    """
    def get_input_frame(self):
        return self._input_frame
    """
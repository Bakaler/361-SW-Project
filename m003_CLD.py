from tkinter import *

class CLDisplay:
    """
    GUI front face to display command line

    Stores command string
    """

    def __init__(self, root):
        self._commandLine = StringVar()
        self.set_command_line("0")

        self._command_frame = Frame(root, width=390, height=50, bg = '#e3f0f0')
        self._command_frame.pack(side=TOP)

        self._command_field = Label(self._command_frame, font=('ariel', 18, 'bold'),
                                    textvariable=self._commandLine, width=50,
                                    bg='#e3f0f0', bd=0, anchor="e")
        self._command_field.grid(row=0, column=0)
        self._command_field.pack(ipady=5)

    def get_command_line(self):
        """
        Return current command line
        """
        return self._commandLine

    def set_command_line(self, expression):
        """
        Update / Set command line
        """
        self._commandLine.set(expression)

    def set_color(self, color : str) -> None:
        self._command_field.config(bg = color)
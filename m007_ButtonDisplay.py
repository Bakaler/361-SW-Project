from tkinter import *

class ButtonDisplay:

    def __init__(self, root, calculator):
        self._calculator = calculator

        self._colorMain = "#b5b3c2"
        self._colorOff = "#ceccd9"
        self._btns_frame = Frame(root, width=390, height=300, bg="grey")
        self._btns_frame.pack(side = BOTTOM)

        self._secondary = False
        self._clear = StringVar()
        self._clear.set("CE")
        self._buttons = self.Buttons()

    def Buttons(self):
        self._b1 = Button(self._btns_frame, text = "2nd", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self.secondary_functions(
                        )).grid(row = 0, column = 0, padx = 1, pady = 1)

        self._b2 = Button(self._btns_frame, text = "1/x", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "recip()")).grid(row = 0, column = 1, padx = 1, pady = 1)

        self._b3 = Button(self._btns_frame, text = "|x|", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "abs()")).grid(row = 0, column = 2, padx = 1, pady = 1)

        # Special Cases, button switches between C and CE

        self._b4 = Button(self._btns_frame, text="C", fg="black", width=10, height=3, bd=0,
                        bg=self.get_colorOff(), cursor="hand2", command=lambda: self._calculator.clear_all(
                        )).grid(row=0, column=3, padx=1, pady=1)

        self._b5 = Button(self._btns_frame, text = "Delete", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "Delete")).grid(row = 0, column = 4, padx = 1, pady = 1)

        # Row 2
        self._b6 = Button(self._btns_frame, text = "Sqrt()", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "sqrt()")).grid(row = 1, column = 0, padx = 1, pady = 1)

        self._b7 = Button(self._btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "(")).grid(row = 1, column = 1, padx = 1, pady = 1)

        self._b8 = Button(self._btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        ")")).grid(row = 1, column = 2, padx = 1, pady = 1)

        self._b9 = Button(self._btns_frame, text = "n!", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "fact()")).grid(row = 1, column = 3, padx = 1, pady = 1)

        self._b10 = Button(self._btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "/")).grid(row = 1, column = 4, padx = 1, pady = 1)

        # Row 3
        self._b11 = Button(self._btns_frame, text = "x^y", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "**")).grid(row = 2,  column = 0, padx = 1, pady = 1)

        self._b12 = Button(self._btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "7")).grid(row = 2, column = 1, padx = 1, pady = 1)

        self._b13 = Button(self._btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "8")).grid(row = 2, column = 2, padx = 1, pady = 1)

        self._b14 = Button(self._btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "9")).grid(row = 2, column = 3, padx = 1, pady = 1)

        self._b15 = Button(self._btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "*")).grid(row = 2, column = 4, padx = 1, pady = 1)

        # Row 4
        self._b16 = Button(self._btns_frame, text = "10^y", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "TenPoY()")).grid(row = 3,column = 0, padx = 1, pady = 1)

        self._b17 = Button(self._btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "4")).grid(row = 3,  column = 1, padx = 1, pady = 1)

        self._b18 = Button(self._btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "5")).grid(row = 3, column = 2, padx = 1, pady = 1)

        self._b19 = Button(self._btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "6")).grid(row = 3, column = 3, padx = 1, pady = 1)

        self._b20 = Button(self._btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "-")).grid(row = 3, column = 4, padx = 1, pady = 1)

        # Row 5
        self._b21 = Button(self._btns_frame, text = "log(n)", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "log()")).grid(row = 4, column = 0, padx = 1, pady = 1)

        self._b22 = Button(self._btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "1")).grid(row = 4,  column = 1, padx = 1, pady = 1)

        self._b23 = Button(self._btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "2")).grid(row = 4, column = 2, padx = 1, pady = 1)

        self._b24 = Button(self._btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "3")).grid(row = 4, column = 3, padx = 1, pady = 1)

        self._b25 = Button(self._btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "+")).grid(row = 4, column = 4, padx = 1, pady = 1)

        # Row 6
        self._b26 = Button(self._btns_frame, text = "x^2", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "square()")).grid(row = 5, column = 0, padx = 1, pady = 1)

        #TODO Figure out how were going to implement sign changes
        self._b27 = Button(self._btns_frame, text = "+/-", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "neg()")).grid(row = 5, column = 1, padx = 1, pady = 1)

        self._b28 = Button(self._btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "0")).grid(row = 5, column = 2, padx = 1, pady = 1)

        self._b29 = Button(self._btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        ".")).grid(row = 5, column = 3, padx = 1, pady = 1)

        self._b30 = Button(self._btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorOff(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "=")).grid(row = 5, column = 4, padx = 1, pady = 1)

    def get_colorMain(self):
        return self._colorMain

    def get_colorOff(self):
        return self._colorOff

    def set_color(self, main : str, off : str) -> None:
        """
        Update / Set button function

        :params:
            main    -   set main color hex color
            off     -   set off color hex code

        """
        self._colorMain = main
        self._colorOff = off
        self._buttons = self.Buttons()

    def get_clear(self)-> None:
        """
        return clear status
        """
        return self._clear

    def secondary_functions(self)-> None:
        """
        Switch 2ndary function column

        """
        if self._secondary == False:
            self._secondary = True
            self._b6 = Button(self._btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "3.14")).grid(row = 1, column = 0, padx = 1, pady = 1)
            self._b11 = Button(self._btns_frame, text = "**", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "**")).grid(row = 2,  column = 0, padx = 1, pady = 1)
            self._b16 = Button(self._btns_frame, text = "//", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "//")).grid(row = 3,column = 0, padx = 1, pady = 1)
            self._b21 = Button(self._btns_frame, text = "%", fg = "black", width = 10, height = 3, bd = 0,
                        bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                        "%")).grid(row = 4, column = 0, padx = 1, pady = 1)
            return

        self._secondary = False
        self._b6 = Button(self._btns_frame, text = "Sqrt(x)", fg = "black", width = 10, height = 3, bd = 0,
                    bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                    "sqrt()")).grid(row = 1, column = 0, padx = 1, pady = 1)
        self._b11 = Button(self._btns_frame, text = "x^y", fg = "black", width = 10, height = 3, bd = 0,
                    bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                    "**")).grid(row = 2,  column = 0, padx = 1, pady = 1)
        self._b16 = Button(self._btns_frame, text = "10^y", fg = "black", width = 10, height = 3, bd = 0,
                    bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                    "TenPoY()")).grid(row = 3,column = 0, padx = 1, pady = 1)
        self._b21 = Button(self._btns_frame, text = "log(n)", fg = "black", width = 10, height = 3, bd = 0,
                    bg = self.get_colorMain(), cursor = "hand2", command = lambda: self._calculator.recieve_input(
                    "log()")).grid(row = 4, column = 0, padx = 1, pady = 1)


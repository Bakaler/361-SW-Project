from tkinter import *

class TabDisplay:

    def __init__(self, root, calculator):
        self._calculator = calculator

        self._tab_frame = Frame(root, width=312, height=15)
        self._tab_frame.pack(side=TOP, padx = 10, anchor = NW)

        self._buttons = self.buttons()


    def buttons(self):
        self._colors = Button(self._tab_frame, text = "Colors", width=10, height =1, bd = 0,
                            bg = "#e3f0f0", cursor = "hand1", command = None).grid(row=0, column=0, padx=0, pady=0)

        self._history = Button(self._tab_frame, text = "History", width=10, height =1, bd = 0,
                            bg = "#e3f0f0", cursor = "hand1", command = None).grid(row=0, column=1, padx=0, pady=0)

        self._graphing = Button(self._tab_frame, text = "Graphing", width=10, height =1, bd = 0,
                            bg = "#e3f0f0", cursor = "hand1", command = None).grid(row=0, column=2, padx=0, pady=0)

        self._history = Button(self._tab_frame, text = "About", width=10, height =1, bd = 0,
                            bg = "#e3f0f0", cursor = "hand1", command = None).grid(row=0, column=3, padx=0, pady=0)
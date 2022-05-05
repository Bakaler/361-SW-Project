from tkinter import *

class Functions:

    def __init__(self):
        self._text = StringVar()

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text.set(text)
        return self._text

    def btn_click(self, item):
        '''
        btn_function updates the input field whenever a number is entered
        param item:
        :return:
        '''
        global expression
        expression = expression + str(item)
        self._text.set(expression)
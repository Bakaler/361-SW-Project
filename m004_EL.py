import re

class EquationLine:

    def __init__(self, ELDisplay : object) -> None:
        '''
        Equation is stored as a string
            '1 + 1/100 + 8'
        newEquation is used whenever the user presses "=" indicating to clear and update the Equation string
        '''
        self._equation = ""
        self._newEquation = False
        self._ELDisplay = ELDisplay()

    def get_equation(self):
        '''
        :return: EL string
        '''
        return self._equation

    #TODO Cleaned
    def update_equation(self, value, solve = False):
        '''
        :param value: integer value from CL to be pushed
        :return: Adds the CL integer to the right most of the EL string
        '''
        if solve is True:
            self._equation = str(value)
            self._ELDisplay.set_equationLine(self._equation)
            return

        if re.match('-\d', value):
            value = f"({value})"

        self._equation += str(value)
        self._ELDisplay.set_equationLine(self._equation)


    def front_parenthesis_buffer(self):
        self._equation = f"{self._equation[:0]}({self._equation[0:]}"

        #TODO Above is UNTESTED, below is original
        #self._equation = self._equation[:0] + "(" + self._equation[0:]

    def clear_equation(self):
        '''
        :return: Resets the EL to a blank state
        '''
        self._equation = ""
        self._ELDisplay.set_equationLine(self._equation)

    def set_switch(self, Boolean):
        '''
        :return: Sets newEquation to True or False
        '''
        self._newEquation = Boolean

    def get_switch(self):
        '''
        returns True or False, depending on EL clear
        '''
        return self._newEquation


    #TODO REMOVED
    # Added into update_equation
    """
    def solve_and_update_ELD(self, solution):
        '''
        Solve equation and update EL
        This function is used only when the "=" is used right before a function call
        9 -> + -> 3 -> = -> Sqrt(x)
        '''
        self._equation = str(solution)
        self._ELDisplay.set_equationLine(self._equation)
    """
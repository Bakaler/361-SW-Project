class EquationLine:

    def __init__(self, ELDisplay : object) -> None:
        self._equationLine = ""
        self._ELDisplay = ELDisplay

    def get_equation_line(self) -> str:
        '''
        :return: EL string
        '''
        return self._equationLine

    def set_equation_line(self, equation : str) -> None:
        '''
        Update // set equation
        '''
        self._equationLine = equation
        self.update_ELDisplay()

    def update_ELDisplay(self) -> None:
        '''
        Update the equation line display to match self._equationLine
        '''
        self._ELDisplay.set_equation_line(self._equationLine)

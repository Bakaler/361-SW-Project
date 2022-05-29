class CommandLine:

    def __init__(self, CLDisplay : object) -> None:
        self._commandLine = ""
        self._CLDisplay = CLDisplay

    def get_command_line(self) -> str:
        '''
        :return: CL string
        '''
        return self._commandLine

    def set_command_line(self, command : str) -> None:
        '''
        Update // set command
        '''
        self._commandLine = command
        self.update_CLDisplay()

    def update_CLDisplay(self) -> None:
        '''
        Update the command line display to match self._equationLine
        '''
        self._CLDisplay.set_command_line(self._commandLine)

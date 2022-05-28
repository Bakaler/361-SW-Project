import re
from g001_Functions import *

class EBNF_parser:

    def __init__(self, functionMap : dict) -> None:
        self._equationLine : str = ""
        self._equationLineFlag : bool = False

        self._commandLine : str = ""
        self._commandLineFlag : bool = True

        self._userInput  : str = ""
        self._trailingInput = [False]

        self._errorStatus = False

        # Key : List[Regex String, Input String]
        self._functionMap : dict = functionMap
        self._operands = {"+", "-", "*", "**", "/", "%", "//"}


    def parse(self, userInput : str, equationLine : str, commandLine : str):
        if self._errorStatus == True:
            self._errorStatus = False
            equationLine = ""
            commandLine = "0"
        self.update_class_variables(userInput, equationLine, commandLine)

        # (Type, userInput)
        result = self._exp(userInput)

        if result[0] != False:

            self.update_lines(result[0], result[1])

            return(True, self._equationLine, self._commandLine)

        return(False, self._equationLine, self._commandLine)


    def update_class_variables(self, userInput : str, equationLine : str, commandLine : str) -> None:
        self._userInput  = userInput

        if (userInput.isdigit() or userInput == "." ) and  "=" in self._equationLine:
            self._commandLine = ""
            self._equationLine = ""

        elif userInput in self._operands and "=" in self._equationLine:
            self._equationLine = self._commandLine

        elif userInput == "(" and "=" in self._equationLine:
            self._equationLine = self._commandLine

        else:
            self._commandLine = commandLine
            self._equationLine = equationLine

        if self._equationLine:
            trailingInput = re.search(r'\S*\s?$', self._equationLine)
            self._trailingInput = self._equationLine[trailingInput.span()[0]: trailingInput.span()[1]]
            self._trailingInput = self._trailingInput.strip()
            return

        self._trailingInput = [False]


    def update_lines(self, commandType : str, commandInput : str):

        if commandInput == "=":
            self.solve()
            return

        if commandType == "Function":
            self._equationLine = self.buffer_floating_decimal(self._equationLine)
            self._equationLine += commandInput
            try:
                self.update_command_line(str(eval(f'{commandInput}')), True)
            except OverflowError:
                self._errorStatus = True
                self._commandLine = "Math range error"
                return
            except SyntaxError:
                print("!")
                parans = self.get_paranBalance()
                print(parans)
                while parans != 0:
                    commandInput += ")"
                    parans -= 1
                    #print(commandInput)
                self.update_command_line(str(eval(f'{commandInput}')), True)

        else:
            if not commandInput.isdigit():
                self._equationLine = self.buffer_floating_decimal(self._equationLine)
            if self._equationLineFlag is True and commandInput == "(":
                self._equationLine = commandInput
            else:
                if self._trailingInput == "0" and commandInput == "0":
                    return
                self._equationLine += commandInput
            self._equationLineFlag = False

        if commandType == "SoloDec":
            self._commandLineFlag = False
            self.update_command_line("0.", True)

        if commandType == "Factor":
            self.update_command_line("0", True)

        if commandType == "Digit":
            if self._commandLineFlag:
                self.update_command_line(commandInput, True)
                self._commandLineFlag = False
            else:
                self.update_command_line(commandInput)

        else:
            self._commandLineFlag = True
            if self._commandLine and self._commandLine[-1] == ".":
                self.update_command_line("0", True)


    def update_command_line(self, commandInput : str, replace = False) -> None:
        if commandInput is None:
            pass

        elif replace:
            if re.search(r'\.', commandInput):
                ll = re.search(r'\.0*$', commandInput)
                if ll:
                    self._commandLine = commandInput[:ll.span()[0]]
            else:
                self._commandLine = commandInput

        else:
            self._commandLine += commandInput


    def buffer_floating_decimal(self, line):
        if len(line) > 0 and line[-1] == ".":
            return line[:-1]
        return line


    def update_function(self, commandInput : str) -> None:

        trailingInput = re.search(r'\S*\s?$', self._equationLine)
        # Removes integer from equation and adds it to function
        move = self._equationLine[trailingInput.span()[0]: trailingInput.span()[1]]

        # Stores trimmed front values
        frontBuffer = ""

        # If the lastline is a function
        for func in self._functionMap.values():
            if self.inspect(func[0], move):
                self._equationLine = self._equationLine[:len(self._equationLine)-(trailingInput.span()[1]- trailingInput.span()[0])]
                self._equationLine += f'{frontBuffer}{self._functionMap[commandInput][1]}{move})'
                return

        # Any other case
        while not self._function(move)[0] and move:
            frontBuffer += move[0]
            move = move[1:]

        self._equationLine = self._equationLine[:len(self._equationLine)-(trailingInput.span()[1]- trailingInput.span()[0])]
        self._equationLine += f'{frontBuffer}{self._functionMap[commandInput][1]}{move})'


    def get_paranBalance(self) -> int:
        """
        Returns the paranthesis balance
        Positive is "(" heavy. Can't be negative
        """
        balance = 0
        for x in self._equationLine:
            if x == "(":
                balance += 1
            elif x == ")":
                balance -= 1
        return balance


    def solve(self):
        """
        Evaulates and Solves the equation
        """
        self._equationLineFlag = True

        if self._equationLine == "":
            return

        self.auto_fill_equation()

        if self._trailingInput == "=":
            self.flatten_function()
            self.recurssive_solve()
        else:
            self._equationLine += " ="

        try:
            solution = eval(self._equationLine[:-1])
            if len(str(solution)) > 20:
                solution = "{:.15e}".format(float(solution))
            solution = str(solution)

            if re.search(r'\d\.0+$' ,solution):
                temp = re.search(r'\d\.0+$' ,solution)
                solution = solution[:temp.span()[0]+1]

            self._commandLine  =  solution
            self._commandLineFlag = True

        except ZeroDivisionError:
            self._errorStatus = True
            self._commandLine = "Cannot divide by zero"

        except OverflowError:
            self._errorStatus = True
            self._commandLine = "Math range error"



    def recurssive_solve(self):
        first = re.search(r'^\d*', self._equationLine)
        self._equationLine = self._equationLine[first.span()[1]:]

        self._equationLine = self._commandLine + self._equationLine


    def flatten_function(self):
        searching = re.search(r'\S*', self._equationLine)
        inspect = self._equationLine[searching.span()[0]: searching.span()[1]]

        return_line = ""

        while inspect:

            inspect = self._equationLine[searching.span()[0]: searching.span()[1]]

            if inspect.isdigit():
                self._equationLine = self._equationLine[len(inspect)+1:]
                return_line += inspect + " "
                searching = re.search(r'\S*', self._equationLine)
                inspect = self._equationLine[searching.span()[0]: searching.span()[1]]

            elif inspect in {"+", "-", "*", "**", "/", "%", "//", "="}:
                self._equationLine = self._equationLine[len(inspect)+1:]
                if inspect == "=":
                    return_line += inspect
                else:
                    return_line += inspect + " "
                searching = re.search(r'\S*', self._equationLine)
                inspect = self._equationLine[searching.span()[0]: searching.span()[1]]

            else:
                self._equationLine = self._equationLine[len(inspect)+1:]
                inspect = str(eval(inspect))
                return_line += inspect + " "
                searching = re.search(r'\S*', self._equationLine)
                inspect = self._equationLine[searching.span()[0]: searching.span()[1]]

        self._equationLine = return_line


    def auto_fill_equation(self):
        """
        Idiot Proof the equation
        Fills any left out information in the equation
        Balances Parans
        Buffers decimals
        """

        # Buffers any flaoting decimals (0. <-)
        self._equationLine = self.buffer_floating_decimal(self._equationLine)

        trailingInput = re.search(r'\S*\s?\S*$', self._equationLine)
        trailingInput = self._equationLine[trailingInput.span()[0]: trailingInput.span()[1]]

        # If last value is an open param, buffer with digit
        if trailingInput[-1] == "(" or trailingInput[-1] == " ":
            if self._commandLine:
                self._equationLine += self._commandLine
            else:
                self._equationLine += "0"

        self._equationLine = self.buffer_floating_decimal(self._equationLine)

        # Balance Parathesis
        count = self.get_paranBalance()
        while count != 0:
            self._equationLine += ")"
            count -= 1

        trailingInput = re.search(r'\S*$', self._equationLine)
        trailingInput = self._equationLine[trailingInput.span()[0]: trailingInput.span()[1]]

        # Special edge case. Sloppy
        #TODO Improve this off ass thing...
        if not self._power(trailingInput)[0] and not self._power(trailingInput):
            self.update_command_line(self.buffer_floating_decimal(self._commandLine), True)
            self._equationLine += self._commandLine


    def _exp(self, userInput : str) -> tuple[bool or str, None or str]:
        """
        _exp ::=
            '='
            exp '+' term
            exp '-' term
            term
        """
        if userInput == "=":
            return ("Solve", userInput)

        # Case userInput is a summation or subtraction
        if self.inspect(r'[\-\+]', userInput):
            if self._trailingInput[0] is False:
                return (False, None)
            if self._trailingInput[-1] == "(":
                return (False, None)
            if self._trailingInput in self._operands:
                self._equationLine = self._equationLine[:len(self._equationLine)-len(self._trailingInput)-2]
                return("Exp", f' {userInput} ')
            if self._trailingInput[-1] == ")":
                return ("Exp", f' {userInput} ')
            if (self._exp(self._trailingInput)[0] or self._exp(self._trailingInput[-1])[0]):
                return ("Exp", f' {userInput} ')

        # Else
        return self._term(userInput)


    def _term(self, userInput : str) -> tuple[bool or str, None or str]:
        """
        _term ::=
            term '*' factor
            term '/' factor
            term '//' factor
            term '%' factor
            factor
        """

        # Case userInput is a Production (or friends)
        if userInput in {'*', '/', '//', '%'}:
            if self._trailingInput[0] is False:
                return (False, None)
            if self._trailingInput[-1] == "(":
                return (False, None)
            if self._trailingInput in self._operands:
                self._equationLine = self._equationLine[:len(self._equationLine)-len(self._trailingInput)-2]
                return("Term", f' {userInput} ')
            if self._trailingInput[-1] == ")":
                return ("Term", f' {userInput} ')
            if (self._term(self._trailingInput)[0] or self._term(self._trailingInput[-1])[0]):
                return ("Term", f' {userInput} ')

        # Else
        return self._factor(userInput)


    def _factor(self, userInput : str) -> tuple[bool or str, None or str]:
        """
            '(' exp ')'
            power
        """

        # Open paranthesis
        if userInput == "(":
            if self._trailingInput == "=":
                return ("Factor" , userInput)
            if self._trailingInput[0] is False or self._trailingInput[-1] == "(":
                return ("Factor" , userInput)
            if (self._trailingInput[-1] == ")" or (self._function(self._trailingInput)[0])):
                if self._equationLineFlag:
                    return ("Factor", userInput)
                return ("Factor" , f' * {userInput}')
            if self._trailingInput in self._operands:
                return ("Factor" , userInput)

            # Case unable to implement
            return (False, None)

        # Closed paranthesis
        elif userInput == ")":
            if self.get_paranBalance() > 0:
                if self._trailingInput and self._trailingInput[-1] == "(":
                    return ("Factor", f'0{userInput}')
                if self._trailingInput in self._operands:
                    return (False, None)
                return ("Factor", userInput)
            # Case unable to implement
            return (False, None)

        return self._power(userInput)


    def _power(self, userInput) -> tuple[bool or str, None or str]:
        """
        _power ::=
            power '**' factor
            function
        """

        # Case command is exponential
        if self.inspect(r'\*{2}', userInput):
            if self._trailingInput in self._operands:
                self._equationLine = self._equationLine[:len(self._equationLine)-len(self._trailingInput)-2]
                return("Power", f' {userInput} ')
            if (self._power(self._trailingInput)[0] or self._power(self._trailingInput[-1])[0]):
                return ("Power", f' {userInput} ')
            if self._trailingInput[-1] == ")":
                return ("Power", f' {userInput} ')

        # Else
        return self._function(userInput)


    def _function(self, userInput) -> tuple[bool or str, None or str]:
        """
        _function ::=
            [digit | function ] [abs | sqrt | 1/x | n! | 10^y | x^y | log | neg]
            digit
        """

        # We are implementing a function
        if userInput in self._functionMap:
            # In the case userInput is a function and the trailing input is a nested funciton
            if (self._trailingInput[0] not in self._operands and self._equationLine) and self._trailingInput[0] != "(":
                ll = re.search(r'\s*\w*\(.*\)$', self._equationLine)
                if not ll:
                    ll = re.search(r'\S*$', self._equationLine)
                temp_trail = self._equationLine[ll.span()[0]:]
                if temp_trail[0] == " ":
                    temp_trail = temp_trail[1:]
                self._equationLine = self._equationLine[:ll.span()[0]]
                if temp_trail[-1] == ".":
                    return ("Function", self._functionMap[userInput][1]+temp_trail[:-1]+")")
                return ("Function", self._functionMap[userInput][1]+temp_trail+")")

            # Any other than above we use what exist in the command line
            else:
                ll = re.search(r'[\d|\.]*$', self._equationLine)
                self._equationLine = self._equationLine[:ll.span()[0]]
                if self._commandLine == "":
                    self._commandLine = "0"
                return ("Function", self._functionMap[userInput][1]+self._commandLine+")")

        # Else
        return self._digit(userInput)


    def _digit(self, userInput) -> tuple[bool or str, None or str]:
        """
        _digit ::=
            int '.' int
            int
        """

        # Case command is an integer
        if self._trailingInput[-1] == ")":
            return (False, userInput)

        if self.inspect(r'^\d+', userInput):
            return ("Digit", userInput)

        # Case command is a decimal
        elif self.inspect(r'\.', userInput):
            # Case a decimal already exist
            if self.inspect(r'\d+\.\d*', self._trailingInput):
                return (False, userInput)
            # Case a decimal doesn't exist
            elif self.inspect(r'\d+', self._trailingInput):
                return ("Digit", userInput)
            # Case we need to buffer a 0
            elif self._trailingInput[0] is False or self.inspect(r'\s?\S*$', self._trailingInput):
                return ("SoloDec", f'0{userInput}')

        # Else
        return (False, userInput)


    def inspect(self, regex, against) -> object or bool:
        """
        Regex against 'against'

        params:
            regex   :   Regular Expression for Comparison
            against :   String to compare against

        returns:
            object - Represents True
            bool   - Represents False
        """

        if against is not None and against[0] is not False:
            return re.search(regex, against)
        return False
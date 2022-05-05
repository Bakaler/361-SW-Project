import re
from os import *
from math import sqrt

class Calculator:

    def __init__(self):
        self.parser = EBNF()
        # Entire up to point equation
        self.equation = ""
        # Lsat digit/float to be entered
        self.current = ""
        # Entered command by user
        self.command = ""
        self.functions = {"abs()", "sqrt()"}

    def user_input(self, userCommand):
        update = self.parser.parse(userCommand, self.equation)
        if update:
            if update in self.functions:
                self.equation = self.buffer_floating_decimal(self.equation)
                self.update_function(update)
            else:
                if not update.isdigit():
                    self.equation = self.buffer_floating_decimal(self.equation)
                self.equation += update

            if update.isdigit() or self.is_float(update):
                self.current = update

    def is_float(self, string):
        try:
            float(string)
            return True
        except:
            return False

    def buffer_floating_decimal(self, line):
        if len(line) > 0 and line[-1] == ".":
            return line + "0"
        return line

    def solve(self):
        self.equation = self.buffer_floating_decimal(self.equation)
        count = self.parser.get_paranBalance()
        while count != 0:
            self.equation += ")"
            count -= 1

        # Check if last is a digit or function
        last = re.search(r'\S*\s?\S*$', self.equation)
        last = self.equation[last.span()[0]: last.span()[1]]
        if self.parser._digit(last)[0]:
            solution = eval(self.equation)
            print(self.equation, " = ", solution)
        elif self.parser._function(last)[0]:
            solution = eval(self.equation)
            print(self.equation, " = ", solution)
        else:
            self.current = self.buffer_floating_decimal(self.current)
            solution = eval(self.equation + self.current)
            print(self.equation + self.current, " = ", solution)

        sciCalc.equation =''

    def update_function(self, update):
        myFunctions = { "abs()" : "abs(",
                        "sqrt()": "sqrt(",
                        ""      : ""}

        ll = re.search(r'\S*$', self.equation)
        # Removes integer from equation and adds it to function
        move = self.equation[ll.span()[0]: ll.span()[1]]
        self.equation = self.equation[:len(self.equation)-(ll.span()[1]- ll.span()[0])]
        self.equation += f'{myFunctions[update]}{move})'


class EBNF:

    def __init__(self):
        self.equation = ""
        self.command = ""
        self.lastline = None
        self.functions = {"abs()", "sqrt()"}
        # Positive = (
        # Negative = )
        self.paranBalance = 0

    def get_paranBalance(self):
        return self.paranBalance

    def update_params(self, command : str, equation : str) -> None:
        """
        Updates the class variables to match calculators

        :params:
            command     - Current users button input
            equation    - Current workable equation
        """
        self.equation = equation
        self.command = command

        ll = re.search(r'\s?\S*$', self.equation)
        if ll:
            self.lastline = self.equation[ll.span()[0]: ll.span()[1]]
            return
        else:
            self.lastline = None
            return

    def parse(self, command, equation) -> str or None:
        self.update_params(command, equation)
        print(self.lastline)

        result = self._exp(command)
        print(result)
        if result[0] != False:
            if result[0] == "Float" or result[0] == "Int":
                return command
            elif result[0] == "Factor":
                return command
            elif result[0] == "SoloDec":
                return f'0{command}'
            # abs(), sqrt(), etc...
            if result[1] in self.functions:
                return command
            else:
                return f" {command} "
        return None

    def _exp(self, command, factor = False):
        """
        exp '+' term
        exp '-' term
        term
        """

        #if self.equation == '':
        #    return self._term(command)

        #if command == "+" or command == "-":
        if self.inspect(r'[\-\+]', command):
            if self.lastline and self._exp(self.lastline)[0]:
                #if self._exp(self.lastline)[0]:
                return ("Exp", command)
            #if self.inspect(r'[\-]', command):
                #if self._factor(command)[0]:
                #return self._factor(command)[0]

        return self._term(command)

    def _term(self, command):
        """
        _term ::=
            term '*' factor
            term '/' factor
            term '//' factor
            term '%' factor
            factor
        """
        if command in {'*', '/', '//', '%'}:
            if self.lastline and self._term(self.lastline)[0]:
                #if self._term(self.lastline)[0]:
                return ("term", command)

        return self._factor(command)

    def _factor(self, command):
        """
            '(' exp ')'
            '-' factor
        """
        if command == "(":
            if self.lastline == "" or self.lastline[-1] != ")":
                self.paranBalance += 1
                return ("Factor" , command)
            return (False, None)
        elif command == ")":
            if self.paranBalance > 0 and (self.lastline == "" or self.lastline[-1] != "("):
                self.paranBalance -= 1
                return ("Factor", command)
            return (False, None)
        #elif command == "-":
        #    if self.lastline == "" or self.lastline[-1] == " ":
        #        return ("Factor", command)
        #    else:
        #        return (False, None)

        return self._function(command)

    def _function(self, command):
        """
        _function ::=
            [digit | function ] [abs | sqrt | 1/x | n! | 10^y | x^y | log]
        """
        # + -25abs() -> + abs(-25)

        myFunctions = { "abs()" : "abs\(\.*\)",
                "sqrt()": "sqrt\(\.*\)",
                ""      : ""}
        if command in myFunctions:
            if self.lastline and self._function(self.lastline)[0]:
                return ("function", command)
            else:
                return (False, command)

        return self._digit(command)

    def _digit(self, command):
        """
        int . int
        int
        """
        if self.inspect(r'\d+', command):
            return ("Int", command)
        elif self.inspect(r'\.', command):
            if self.inspect(r'\d+\.\d*', self.lastline):
                return (False, command)
            elif self.inspect(r'\d+', self.lastline):
                return ("Float", command)
            elif self.lastline == "" or self.inspect(r'\s?\S*$', self.lastline):
                return ("SoloDec", command)


        return (False, command)

    def inspect(self, regex, against):

        if against is not None:
            return re.search(regex, against)
        return False


if __name__ == "__main__":

    sciCalc = Calculator()

    while True:
        userInput = input()
        if userInput == "exit":
            if name == 'nt':
                _ = system('cls')
            break
        if userInput == 'cls':
            sciCalc.equation =''
            if name == 'nt':
                _ = system('cls')
            continue
        if userInput == 'solve':
            sciCalc.solve()
            continue

        sciCalc.user_input(userInput)
        print(f"Equation = {sciCalc.equation}")
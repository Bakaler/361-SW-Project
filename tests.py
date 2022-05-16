import unittest
from tkinter import Tk
import m001_main


class TestCase(unittest.TestCase):
    root = Tk()
    sciCalc = m001_main.Calculator(root)

    def test1EL(self):
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "0 + 0 =")
        self.sciCalc.clear_all()

    def test1CL(self):
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test2EL(self):
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "0 + 0 =")
        self.sciCalc.clear_all()

    def test2CL(self):
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test3EL(self):
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "abs(0) =")
        self.sciCalc.clear_all()

    def test3CL(self):
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test4EL(self):
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "0 + 0 + 0 =")
        self.sciCalc.clear_all()

    def test4CL(self):
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test5EL(self):
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("2")
        self.sciCalc.recieve_input("3")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("4")
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "1.2345 =")
        self.sciCalc.clear_all()

    def test5CL(self):
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("2")
        self.sciCalc.recieve_input("3")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("4")
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "1.2345")
        self.sciCalc.clear_all()


    def test6EL(self):
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "abs(0) + 11 + 11 =")
        self.sciCalc.clear_all()

    def test6CL(self):
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "22")
        self.sciCalc.clear_all()

    def test7EL(self):
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("9")
        self.sciCalc.recieve_input("neg()")
        self.sciCalc.recieve_input("%")
        self.sciCalc.recieve_input("3")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "5 * (neg(9) % 3 * (0)) =")
        self.sciCalc.clear_all()


    def test7CL(self):
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("9")
        self.sciCalc.recieve_input("neg()")
        self.sciCalc.recieve_input("%")
        self.sciCalc.recieve_input("3")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test8EL(self):
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("**")
        self.sciCalc.recieve_input("10")
        self.sciCalc.recieve_input("square()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "5 ** square(10) =")
        self.sciCalc.clear_all()

    def test8CL(self):
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("**")
        self.sciCalc.recieve_input("10")
        self.sciCalc.recieve_input("square()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "7.888609052210118e+69")
        self.sciCalc.clear_all()

    def test9EL(self):
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "(0) * (0) * ((0) * (0)) =")
        self.sciCalc.clear_all()

    def test9CL(self):
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input(")")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test10EL(self):
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("3")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("neg()")
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "abs(neg(1.53)) =")
        self.sciCalc.clear_all()

    def test10CL(self):
        self.sciCalc.recieve_input("1")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("3")
        self.sciCalc.recieve_input(".")
        self.sciCalc.recieve_input("neg()")
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "1.53")
        self.sciCalc.clear_all()


    def test11EL(self):
        self.sciCalc.recieve_input("2")
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("sqrt()")
        self.sciCalc.recieve_input("-")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "sqrt(25) - 5 =")
        self.sciCalc.clear_all()

    def test11CL(self):
        self.sciCalc.recieve_input("2")
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("sqrt()")
        self.sciCalc.recieve_input("-")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()


    def test12EL(self):
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "5 + (0) =")
        self.sciCalc.clear_all()

    def test12CL(self):
        self.sciCalc.recieve_input("5")
        self.sciCalc.recieve_input("+")
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "5")
        self.sciCalc.clear_all()

    def test13EL(self):
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "(abs(0)) =")
        self.sciCalc.clear_all()

    def test13CL(self):
        self.sciCalc.recieve_input("(")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("abs()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()

    def test14EL(self):
        self.sciCalc.recieve_input("7")
        self.sciCalc.recieve_input("sqrt()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "sqrt(7) =")
        self.sciCalc.clear_all()

    def test14CL(self):
        self.sciCalc.recieve_input("7")
        self.sciCalc.recieve_input("sqrt()")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "2.6457513110645907")
        self.sciCalc.clear_all()

    def test15EL(self):
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_equation_line(), "0 =")
        self.sciCalc.clear_all()

    def test15CL(self):
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("0")
        self.sciCalc.recieve_input("=")
        self.assertEqual(self.sciCalc.get_command_line(), "0")
        self.sciCalc.clear_all()


if __name__ == "__main__":
    unittest.main()

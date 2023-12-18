"""Modules importing a new class Fraction and unitary test for basic python"""
import unittest
from tp_9 import Fraction

# ------------------ Unittest class ------------------


class TestConstructor(unittest.TestCase):
    """This class do unitary test on the constructor (__init__) of fraction's class"""

    def test_construct_positif(self):
        """Test if afraction numerator and denominator are equal to what was given in parameter"""
        self.assertEqual(Fraction(5, 2).numerator == 5, True, "Positif is good")
        self.assertEqual(Fraction(1, 8).denominator == 8, True, "Positif is good")
        self.assertEqual(
            Fraction(12, 5).numerator == 12 and Fraction(12, 5).denominator == 5,
            True,
            "Positif is good",
        )

    def test_concstruct_negatif(self):
        """Test if a fraction numerator and denominator are equal to what was given in parameter"""
        self.assertEqual(
            Fraction(-11, 3).numerator == -11 and Fraction(-11, 3).denominator == 3,
            True,
            "Negative is good",
        )
        self.assertEqual(
            Fraction(7, -2).numerator == 7 and Fraction(7, -2).denominator == -2,
            True,
            "Negative is good",
        )
        self.assertEqual(
            Fraction(-25, -12).numerator == -25
            and Fraction(-25, -12).denominator == -12,
            True,
            "Negative is good",
        )

    def test_construct_zero(self):
        """Raise a error if the denominator is equal to zero"""
        self.assertRaises(ZeroDivisionError, Fraction, 5, 0)
        self.assertRaises(ZeroDivisionError, Fraction, 0, 0)
        self.assertRaises(ZeroDivisionError, Fraction, -5, 0)

    def test_construct_float(self):
        """Test if the float are rounded to his closer integer"""
        self.assertEqual(
            Fraction(12.7, 9.8).numerator == 13
            and Fraction(12.7, 9.8).denominator == 10,
            True,
            "Float is good",
        )
        self.assertEqual(
            Fraction(-12.7, -9.8).numerator == -13
            and Fraction(-12.7, -9.8).denominator == -10,
            True,
            "Float is good",
        )


class TestMixedNumber(unittest.TestCase):
    """This class do unitary test on the as_mixed_number methode of fraction's class"""

    def test_as_mixed_number(self):
        """Test if the returned string correspond"""
        self.assertEqual(
            Fraction(11, 5).as_mixed_number() == "2 + 1/5", True, "Mixed number is good"
        )
        self.assertEqual(
            Fraction(-8, -3).as_mixed_number() == "2 + 2/3",
            True,
            "Mixed number is good",
        )
        self.assertEqual(
            Fraction(-9, 3).as_mixed_number() == "-2 - 1/1",
            True,
            "Mixed number is good",
        )


class TestString(unittest.TestCase):
    """This class do unitary test on the print (__str__) methode of fraction's class"""

    def test_string(self):
        """Test if the __str__ methode return a reduced version of a fraction"""
        self.assertEqual(str(Fraction(10, 5)) == "2/1", True, "String is good")
        self.assertEqual(str(Fraction(-7, 3)) == "-7/3", True, "String is good")
        self.assertEqual(str(Fraction(8.4, 15.9)) == "1/2", True, "String is good")


class TestAdd(unittest.TestCase):
    """This class do unitary test on the addition methode of fraction's class"""
    def test_add(self):
        """Test by adding other fraction as well as integer"""
        self.assertEqual(
            str(Fraction(5, 8) + Fraction(4, 5)) == "57/40",
            True,
            "Addition is good",
        )
        self.assertEqual(
            str(Fraction(10, 3) + Fraction(-7, 5)) == "29/15",
            True,
            "Addition is good",
        )
        self.assertEqual(
            str(Fraction(-17, 7) + Fraction(0, 4)) == "-17/7",
            True,
            "Addition is good",
        )
        self.assertEqual(
            str(Fraction(10, 7) + 2) == "24/7",
            True,
            "Addition is good",
        )

    def test_add_raises(self):
        """Test some unregular value to raise when added"""
        self.assertRaises(TypeError, Fraction(5,2) + "string", "No string")
        self.assertRaises(TypeError, Fraction(5,2) + [], "No string")
        self.assertRaises(TypeError, Fraction(5,2) + 8.4, "No string")

class TestDiv(unittest.TestCase):
    """This class do unitary test on the division methode of fraction's class"""
    def test_true_div(self):
        """Test some regular value to divide by"""
        self.assertEqual(str(Fraction(8, 2) / Fraction(10, 5)) == "2/1", True, "Division is good")
        self.assertEqual(str(Fraction(8, 2) / 2) == "2/1", True, "Division is good")
        self.assertEqual(str(Fraction(3, 9) / Fraction(-2,4)) == "2/-3", True, "Division is good")

    def test_true_div_raises(self):
        """Test unexpected value to raise"""
        self.assertRaises(TypeError, Fraction(3, 2) / "string", "No string")
        self.assertRaises(TypeError, Fraction(3, 2) / [], "No list")
        self.assertRaises(TypeError, Fraction(3, 2) / Fraction(0,3), "No zero")

class TestEqual(unittest.TestCase):
    """This class do unitary test on the equal (__eq__) methode of fraction's class"""
    def test_eq(self):
        """Test if the fraction and the value is equal"""
        self.assertEqual(Fraction(8, 2) == 4, True, "True")
        self.assertEqual(Fraction(11, 3) == Fraction(22, 6), True, "True")
        self.assertEqual(Fraction(-14, 2) == -2, False, "True")

    def test_eq_type(self):
        """Test if a bad-type return a error"""
        self.assertRaises(TypeError, Fraction(6, 7) == "test")
        self.assertRaises(TypeError, Fraction(4, 5) == [4,5])

class TestInteger(unittest.TestCase):
    """This class do unitary test on the is_integer methode of fraction's class"""
    def test_is_zero(self):
        """Test if the fraction is a integer or a float"""
        self.assertEqual(Fraction(8, 2).is_integer(), "Integer", "Its a integer")
        self.assertEqual(Fraction(1, 3).is_integer(), "Float", "It's a float")

class TestProper(unittest.TestCase):
    """This class do unitary test on the is_proper methode of fraction's class"""
    def test_is_proper(self):
        """Test if the absolute value of the fraciton is under 1"""
        self.assertEqual(Fraction(3, 2).is_proper(), "Not proper", "It isn't proper")
        self.assertEqual(Fraction(-8, 11).is_proper(), "Proper", "It's proper")
        self.assertEqual(Fraction(5, 7).is_proper(), "Proper", "I's proper")

class test_is_adjacent_to(unittest.TestCase):
    """This class do unitary test on the is_adjacent_to methode of fraction's class"""
    def test_is_adjacent_to(self):
        """Test if two fraction are adjacent"""
        self.assertEqual(Fraction(8, 5).is_adjacent_to(Fraction(13, 5)), "Under 1", "Adjacent")
        self.assertEqual(Fraction(5, 10).is_adjacent_to(Fraction(4, 2)), "Above 1", "Not adjacent")

    def test_raises_is_adjacent_to(self):
        """Test if other value return a error"""
        self.assertRaises(TypeError, Fraction(2, 1).is_adjacent_to("test"), "No string")
        self.assertRaises(TypeError, Fraction(2, 1).is_adjacent_to([]), "No list")

# ------------------ Main body ------------------

if __name__ == "__main__":
    unittest.main()

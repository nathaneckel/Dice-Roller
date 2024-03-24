#THESE TESTS STILL ARENT WORKING
#
import io
import sys
import unittest
from unittest.mock import patch

from roll import roll_dice


class TestDiceRollingSimulator(unittest.TestCase):
    @patch('random.randint', return_value=3)
    def test_roll_dice_one_die(self, mock_randint):
        with patch('builtins.input', side_effect=['no']):
            captured_output = io.StringIO()  # Create StringIO object to capture output
            sys.stdout = captured_output  # Redirect stdout
            roll_dice()  # Roll one die
            sys.stdout = sys.__stdout__  # Reset redirect
            self.assertEqual(captured_output.getvalue(), "You rolled: 3\n")

    @patch('random.randint', side_effect=[3, 4])
    def test_roll_dice_multiple_dice(self, mock_randint):
        with patch('builtins.input', side_effect=['no']):
            captured_output = io.StringIO()  # Create StringIO object to capture output
            sys.stdout = captured_output  # Redirect stdout
            roll_dice(2)  # Roll two dice
            sys.stdout = sys.__stdout__  # Reset redirect
            self.assertEqual(captured_output.getvalue(), "You rolled: 3\nYou rolled: 4\n")

    @patch('builtins.input', side_effect=['yes', 'no'])
    def test_roll_dice_multiple_rolls(self, mock_input):
        captured_output = io.StringIO()  # Create StringIO object to capture output
        sys.stdout = captured_output  # Redirect stdout
        roll_dice()  # Roll one die
        sys.stdout = sys.__stdout__  # Reset redirect
        output = captured_output.getvalue()
        self.assertIn("You rolled:", output)
        self.assertIn("Roll again?", output)
        self.assertIn("You rolled:", output)
        self.assertNotIn("Roll again?", output)


if __name__ == '__main__':
    unittest.main()

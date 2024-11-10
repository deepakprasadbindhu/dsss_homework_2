import unittest
from math_quiz import generate_random_integer, choose_operator, generate_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # Test if choose_operator returns a valid operator
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random choices
            operator = choose_operator()
            self.assertIn(operator, valid_operators)

    def test_generate_problem(self):
        # Test the correct generation of problems and answers
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()

import random

def generate_random_integer(min_val, max_val):
    """Returns a random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)

def choose_operator():
    """Returns a random operator: '+', '-', or '*'."""
    return random.choice(['+', '-', '*'])

def generate_problem(num1, num2, operator):
    """Creates a math problem and returns it as a string with the correct answer."""
    problem = f"{num1} {operator} {num2}"
    answer = num1 + num2 if operator == '+' else num1 - num2 if operator == '-' else num1 * num2
    return problem, answer

def math_quiz():
    """Runs the math quiz game, presenting math problems and tracking score."""
    score, total_questions = 0, 3
    print("Welcome to the Math Quiz Game! Try to solve each problem.")

    for _ in range(total_questions):
        num1, num2 = generate_random_integer(1, 10), generate_random_integer(1, 5)
        operator = choose_operator()
        problem, answer = generate_problem(num1, num2, operator)
        
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

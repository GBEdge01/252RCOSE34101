
import time
import random
import os
import sys


def timed_input(prompt: str, timeout: float):
    """Prompt for input with a timeout.

    Returns the input string if entered within timeout, otherwise returns None.
    Uses a Windows-friendly `msvcrt` loop when running on Windows; falls back
    to `select` on Unix-like systems.
    """
    if os.name == 'nt':
        import msvcrt

        sys.stdout.write(prompt)
        sys.stdout.flush()
        end_time = time.monotonic() + timeout
        buf = ''
        while time.monotonic() < end_time:
            if msvcrt.kbhit():
                ch = msvcrt.getwche()
                if ch in ('\r', '\n'):
                    sys.stdout.write('\n')
                    return buf
                if ch == '\x08':  # backspace
                    if buf:
                        buf = buf[:-1]
                        sys.stdout.write('\b \b')
                    continue
                buf += ch
            time.sleep(0.01)
        sys.stdout.write('\n')
        return None
    else:
        try:
            import select

            sys.stdout.write(prompt)
            sys.stdout.flush()
            ready, _, _ = select.select([sys.stdin], [], [], timeout)
            if ready:
                line = sys.stdin.readline()
                return line.rstrip('\n')
            else:
                sys.stdout.write('\n')
                return None
        except Exception:
            # Fallback: blocking input (no timeout available)
            return input(prompt)


def calculate_game():
    print("Welcome to the Calculation Game!")
    num_questions = 5
    score = 0

    # Ask user for per-question timeout (default 10 seconds)
    try:
        raw = input("Enter time limit per question in seconds (default 10): ")
        per_question_timeout = int(raw) if raw.strip() else 10
        if per_question_timeout <= 0:
            per_question_timeout = 10
    except Exception:
        per_question_timeout = 10

    for _ in range(num_questions):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct_answer = a + b

        start_time = time.time()
        user_input = timed_input(f"What is {a} + {b}? ", per_question_timeout)
        end_time = time.time()

        if user_input is None:
            print(f"Time's up! The correct answer was {correct_answer}.")
            continue

        try:
            user_answer = int(user_input.strip())
        except Exception:
            print("Invalid input. Counting as incorrect.")
            continue

        if user_answer == correct_answer:
            score += 1
            print(f"Correct! You took {end_time - start_time:.2f} seconds.")
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"Game over! Your score: {score}/{num_questions}")


if __name__ == '__main__':
    calculate_game()
    
    
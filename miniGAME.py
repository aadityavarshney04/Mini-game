import random
import time

def number_game():
    ranges = {1: (0, 9, 3), 2: (10, 99, 6), 3: (100, 999, 10)}
    while True:
        print("\n    Choose a range:")
        print("    1 - 0 to 9")
        print("    2 - 10 to 99")
        print("    3 - 100 to 999")
        try:
            choice = int(input("    Enter your choice: "))
            if choice in ranges:
                break
            else:
                print("    Invalid choice, please select 1, 2, or 3.")
        except ValueError:
            print("    Please enter a valid number.")
    number, attempts = random.randint(ranges[choice][0], ranges[choice][1]), ranges[choice][2]
    print(f"\n    Guess the number between {ranges[choice][0]} and {ranges[choice][1]}!")
    print(f"    You have total {attempts} attempts to guess the number.\n")
    while attempts > 0:
        try:
            guess = int(input("    Enter your guess: "))
            if guess == number:
                print("    Congratulations! You guessed it right!")
                break
            elif guess < number:
                print("    Think Larger. Try again.")
            else:
                print("    Think Smaller. Try again.")
            attempts -= 1
            print(f"    {attempts} attempts left.")
        except ValueError:
            print("    Please enter a valid number.")
    else:
        print(f"    You lost! The correct number was {number}")
    if input("\n    Play again? (y/n): ").strip().lower() == 'y':
        number_game()

def word_game():
    questions = {
        'The only fruit to have seeds on the outside is: ': 'strawberry',
        'Which fruit has no edible skin or seeds? ': 'banana',
        'What is the king of fruits? ': 'mango',
        'A red delicious fruit with the tagline "Once a day will keep the doctor away!"? ': 'apple',
        'What is a dried grape called? ': 'raisin',
        'Which fruit comes in bunches and is most commonly black or green? ': 'grapes',
        'Which fruit has a hard outer surface and contains water inside? ': 'coconut',
        'What is yellow, small-sized, and tastes sour? ': 'lemon',
        'What is juicy, sweet, and my name sounds the same as my color? ': 'orange'
    }
    while True:
        question, answer = random.choice(list(questions.items()))
        print(f"\n    Ques: {question}")
        attempts = 2
        print(f"    You have {attempts} chances to guess\n")
        print(f"    You have total{attempts} attempts")
        while attempts > 0:
            user_input = input("    Enter your answer: ").strip().lower()
            if user_input == answer:
                print("    Yes, correct! You won!")
                break
            else:
                attempts -= 1
                if attempts:
                    print(f"    No, wrong answer. {attempts} chance(s) left.\n")
                else:
                    print(f"    You lost! The correct answer was: {answer}")
        if input("\n    Play again? (y/n): ").strip().lower() != 'y':
            break

def anagram_game():
    words = ['python', 'developer', 'programming', 'challenge', 'gamer', 'puzzle']
    while True:
        chosen_word = random.choice(words)
        shuffled = ''.join(random.sample(chosen_word, len(chosen_word)))
        print(f"\n    Unscramble this word: {shuffled}")
        attempts = 3
        while attempts > 0:
            guess = input("    Your guess: ").strip().lower()
            if guess == chosen_word:
                print("    Correct! You won!")
                break
            else:
                attempts -= 1
                print(f"    Incorrect! {attempts} attempts left.")
        else:
            print(f"    You lost! The correct word was: {chosen_word}")
        if input("\n    Play again? (y/n): ").strip().lower() != 'y':
            break

def memory_challenge():
    words = ['apple', 'banana', 'grape', 'orange', 'mango', 'cherry', 'strawberry']
    while True:
        shown_words = random.sample(words, 5)
        print("\n    Memorize these words (you have 5 seconds):", ', '.join(shown_words))
        time.sleep(5)
        print("\n" * 50 + "    [Screen Cleared - Try to Recall!]")
        recalled_words = set(input("\n    Enter words separated by spaces: ").strip().lower().split())
        correct = len(set(shown_words) & recalled_words)
        if correct == 5:
            print("    Perfect! You remembered all words correctly.")
            print(f"    {', '.join(shown_words)}")
        else:
            print(f"    You remembered {correct} out of 5 words.")
            print(f"    You lost! The correct words were: {', '.join(shown_words)}")
        if input("\n    Play again? (y/n): ").strip().lower() != 'y':
            break

def math_blitz():
    score = 0
    print("\n    Type 'exit' anytime to quit the game.")
    print("    You have 5 seconds to answer each question!")
    while True:
        a, b = random.randint(1, 100), random.randint(1, 10)
        answer = a + b
        start_time = time.time()
        user_input = input(f"\n    {a} + {b} = ").strip().lower()
        if user_input == 'exit':
            print(f"    Exiting Math Blitz... Final Score: {score}")
            break
        if time.time() - start_time > 5:
            print(f"    Time's up! You lose. Final Score: {score}")
            break
        try:
            if int(user_input) == answer:
                print("    Correct!")
                score += 1
            else:
                print(f"    Wrong! The correct answer was {answer}. Final Score: {score}")
                break
        except ValueError:
            print("    Invalid input! Only numbers are allowed.")

def emoji_riddle():
    riddles = {
        "🍎 + 🍌": "fruit salad",
        "⚽ + 🏀": "sports",
        "🐶 + 🐱": "pets",
        "🚗 + 🏍️": "vehicles",
        "📖 + ✏️": "study"
    }
    while True:
        question, answer = random.choice(list(riddles.items()))
        print(f"\n    Guess the phrase: {question}")
        print("    You have 2 attempts to answer.")
        for _ in range(2):
            if input("    Your answer: ").strip().lower() == answer:
                print("    Correct!")
                break
            print("    Try again!")
        else:
            print(f"    You lost! Correct answer: {answer}")
        if input("\n    Play again? (y/n): ").strip().lower() != 'y':
            break

def game():
    while True:
        try:
            val = int(input("\n    Choose a game:\n"
                            "    1 - Number Guessing\n"
                            "    2 - Word Guessing\n"
                            "    3 - Anagram\n"
                            "    4 - Memory Challenge\n"
                            "    5 - Math Blitz\n"
                            "    6 - Emoji Riddle\n"
                            "    0 - Exit\n"
                            "    Enter: "))
            if val == 1:
                number_game()
            elif val == 2:
                word_game()
            elif val == 3:
                anagram_game()
            elif val == 4:
                memory_challenge()
            elif val == 5:
                math_blitz()
            elif val == 6:
                emoji_riddle()
            elif val == 0:
                print("    Thanks for playing!")
                break
            else:
                print("    Invalid choice. Try again.")
        except ValueError:
            print("    Please enter a valid number.")

def menu():
    game()

menu()

import random


display_hangman = [
    """
       -----
       |   |
       |   O /
       |  /|/
       | / |
       | _/ \_
       -
    """,
    """
       -----
       |   |
       |   O /
       |  /|/
       | / |
       | _/ 
       -
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |  
       -
    """,
    """
       -----
       |   |
       |   O
       |  
       |  
       -
    """,
    """
       -----
       |   |
       |   
       |  
       |  
       -
    """,
    """
       -----
       |   
       |   
       |  
       |  
       -
    """,
    ]

WORDS = ['фонарь', 'аптека', 'репозиторий', 'лес', 'индексация', 'интерференция']
def get_random_word():
    return random.choice(WORDS) #Выбирает случайное слово из списка.

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    """Отображает текущее состояние игры."""
    print(hangman_pics[len(missed_letters)])
    print("\nВаши ошибки:", " ".join(missed_letters))
    blanks = ["_" if letter not in correct_letters else letter for letter in secret_word]
    print("\nСлово:", " ".join(blanks))

def main():
    print("Добро пожаловать в игру 'Виселица'!")
    secret_word = get_random_word()
    missed_letters = []
    correct_letters = []
    game_over = False

    while not game_over:
        display_board(display_hangman, missed_letters, correct_letters, secret_word)
        guess = input("\nВведите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in missed_letters + correct_letters:
            print("Вы уже угадывали эту букву! Попробуйте другую.")
            continue

        if guess in secret_word:
            correct_letters.append(guess)
            if all(letter in correct_letters for letter in secret_word):
                display_board(display_hangman, missed_letters, correct_letters, secret_word)
                print("\nПоздравляем! Вы угадали слово:", secret_word)
                game_over = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(display_hangman) - 1:
                display_board(display_hangman, missed_letters, correct_letters, secret_word)
                print("\nВы проиграли! Загаданное слово было:", secret_word)
                game_over = True

    if input("\nХотите сыграть снова? (да/нет): ").lower().startswith("д"):
        main()

if __name__ == "__main__":
    main()
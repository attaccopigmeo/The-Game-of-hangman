import random


def display_hangman(tries):
    stages = [
        """Рисунки сюда, через запятые"""
    ]
    return stages[tries]


def choose_word():
    words = ["идентификатор", "дерево", "друг", "интеллект", "умопомрачительный", "свеча", "огниво"]
    return random.choice(words).upper()


def game():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print('Игра "Виселица"')
    print(display_hangman(tries))

    while tries > 0 and word_letters:
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Слово: " + ' '.join(word_display))
        guess = input("Угадайте букву: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Ошибка ввода. Вводите одну букву.")
            continue
        if guess in guessed_letters:
            print(f"Ужу угадано '{guess}'. Попробуйте снова.")
            continue
        guessed_letters.add(guess)
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Вы угадали! '{guess}' есть в заданном слове.")
        else:
            tries -= 1
            print(f"Неверно! '{guess}' нет в заданном слове. Попыток осталось: {tries}")
        print(display_hangman(tries))
    
    if not word_letters:
        print(f"Поздравляем Вас! Вы угадали слово: {word}")
    else:
        print(f"Вы проиграли! Заданное слово: {word}")


if __name__ == "__main__":
    game()
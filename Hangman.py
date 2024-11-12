import random

WORDS = ["ночь", "улица", "фонарь", "аптека", "дерево", "арбалет", "индульгенция"]


def choose_word(): #Компьютер выбирает рандомное слово из списка
    return random.choice(WORDS)

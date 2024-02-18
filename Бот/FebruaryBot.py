#1. Приветствие
#2. Описание функционала
#3. Генерировать случайную карту
#4. Вопрос пользователю: красная или черная?
#5. Ответ игрока
#6. Сравнение и результат
from random import choice

#1.
print('Hello, player!')

#2.
print('I will generate a random card. You will guess the color of its suit.\n')

#3.
CARD_NUMBER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["H", "D", "S", "C"]

random_card_number = choice(CARD_NUMBER)
random_card_suit = choice(CARD_SUIT)

play_number = int(input('Сколько раз будем играть!: '))
countr = 0
while countr != play_number:
    print(f"Round {countr + 1}")
    player_answer = input("Guess the suit's color of the card: Red or Black: ")
    if 'red' == player_answer.lower() or 'black' == player_answer.lower():
        if player_answer == "red" and random_card_suit in ["H", "D"]:
            print('Correct! The card was: ' + random_card_number + random_card_suit)
        elif player_answer == "black" and random_card_suit in ["S", "C"]:
            print('Correct! The card was: ' + random_card_number + random_card_suit)
        else:
            print('Incorrect! The card was: ' + random_card_number + random_card_suit)
        countr += 1
    else:
        print('Ошибка ввода!')
        break



#1. Проверка на дурака
#2. Уровень сложности.
#3. Внедрение количества раундов (цикл While)
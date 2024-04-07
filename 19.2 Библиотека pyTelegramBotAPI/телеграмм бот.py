import telebot
from config import BIG_TOKEN
from telebot.handler_backends import StatesGroup, State

bot = telebot.TeleBot(BIG_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello world!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_poling()

@bot.message_handler(commands=['start'])
def welcome(message):
    mesg = bot.send_message(message.chat.id, 'Введите имя: ')
    bot.register_next_step_handler(mesg, test)


def test(message):
    name = message.text
    bot.send_message(message.chat.id, f'Ваше имя: {name}')


class My_States(StatesGroup):
    name = State()
    surname = State()
    age = State()


@bot.message_handler(state="*", commands=['cancel'])
def any_state(message):
    """
    Cancel state
    """
    bot.send_message(message.chat.id, "Ваше состояние было отменено")
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=My_States.name)
def name_get(message):
    """
    State 1. Will process when user's state is MyStates.name.
    """
    bot.send_message(message.chat.id, My_States.surname, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['surname'] = message.text


@bot.message_handler(state=My_States.age, is_digit=True)
def ready_for_answer(message):
    """
    State 3. Will process when user's state is My_States.age
    """
    with bot.retrieve_data(message.from_user.id, message.shat.id) as data:
        msg = ("Готово, взгляниет: \n<b>"
               f"Name: {data['name']}\n"
               f"Surname: {data['surname']}\n"
               f"Age: {message.text}<\b>")
        bot.send_message(message.chat.id, msg, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=My_States.age, is_digit=False)
def age_incorrect(message):
    """
    Wrong response for My_States.age
    """
    bot.send_message(message.chat.id, "Похоже вы ввели текстовое значение в поле возраста. Пожалуйста, введите числовое значение.")



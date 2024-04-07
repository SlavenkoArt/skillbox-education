import telebot
from telebot import types

token = "6642246917:AAEIfJex-1UTohVqpiJzcW1Pyi_MuvMVwKo"

bot = telebot.TeleBot(token)

language_list = {"русский": "ru", "азербайджанский": "az", "албанский": "sq", "амхарский": "am",
                 "английский": "en", "арабский": "ar", "армянский": "hy", "африкаанс": "af",
                 "баскский": "eu", "башкирский": "ba", "белорусский": "be", "бенгальский": "bn",
                 "бирманский": "my", "болгарский": "bg", "боснийский": "bs", "валлийский": "cy",
                 "венгерский": "hu", "вьетнамский": "vi", "гаитянский (креольский)": "ht",
                 "галисийский": "gl", "голландский": "nl", "горномарийский": "mrj",
                 "греческий": "el", "грузинский": "ka", "гуджарати": "gu", "датский": "da",
                 "иврит": "he", "идиш": "yi", "индонезийский": "id", "ирландский": "ga",
                 "итальянский": "it", "исландский": "is", "испанский": "es", "казахский": "kk",
                 "каннада": "kn", "каталанский": "ca", "киргизский": "ky", "китайский": "zh",
                 "корейский": "ko", "коса": "xh", "кхмерский": "km", "лаосский": "lo",
                 "латынь": "la", "латышский": "lv", "литовский": "lt", "люксембургский": "lb",
                 "малагасийский": "mg", "малайский": "ms", "малаялам": "ml", "мальтийский": "mt",
                 "македонский": "mk", "маори": "mi", "маратхи": "mr", "марийский": "mhr",
                 "монгольский": "mn", "немецкий": "de", "непальский": "ne", "норвежский": "no",
                 "панджаби": "pa", "папьяменто": "pap", "персидский": "fa", "польский": "pl",
                 "португальский": "pt", "румынский": "ro", "себуанский": "ceb", "сербский": "sr",
                 "сингальский": "si", "словацкий": "sk", "словенский": "sl", "суахили": "sw",
                 "сунданский": "su", "таджикский": "tg", "тайский": "th", "тагальский": "tl",
                 "тамильский": "ta", "татарский": "tt", "телугу": "te", "турецкий": "tr",
                 "удмуртский": "udm", "узбекский": "uz", "украинский": "uk", "урду": "ur",
                 "финский": "fi", "французский": "fr", "хинди": "hi", "хорватский": "hr",
                 "чешский": "cs", "шведский": "sv", "шотландский": "gd", "эстонский": "et",
                 "эсперанто": "eo", "яванский": "jv", "японский": "ja"}

body = {
    "targetLanguageCode": "",
    "texts": "",
    "folderId": "",
}

new_dict = {}


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет {message.from_user.first_name}.')
    markup = types.InlineKeyboardMarkup()
    for elem in language_list:
        markup.add(telebot.types.InlineKeyboardButton(f'{elem}', callback_data=f"{elem}"))
    bot.send_message(message.chat.id, 'Выберите язык', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chosen_language = language_list.get(call.data)
    if chosen_language:
        new_dict[call.message.chat.id] = chosen_language
        bot.send_message(call.message.chat.id, f'Выбран язык: {new_dict})\n Введите текст: ')
    else:
        bot.send_message(call.message.chat.id, f'Выбран недопустимый язык {chosen_language}')


@bot.message_handler(content_types=['text'])
def echo_all(message):
    new_dict["text"] = message.text
    bot.send_message(message.chat.id, f"Введенный текст: {new_dict}")






bot.infinity_polling()

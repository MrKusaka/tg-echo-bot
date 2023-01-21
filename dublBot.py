import telebot
import json

from telebot import types


# токен записан в отдельном файле json
with open('data/keys.json', 'r', encoding='UTF-8') as f:
    bot = telebot.TeleBot(json.load(f)["token"])


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Начать битву!"))
    bot.send_message(message.chat.id, f'Ну привет, <b>{message.from_user.first_name}!</b> '
                                      'В повторении я мастер. Давай проверим, кто первый сдастся?',
                                      parse_mode='html',
                                      reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)

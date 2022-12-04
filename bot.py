import telebot
from config import keys,TOKEN
from utilts import CryptoConvecter, ConvertionException


bot: telebot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['help'])
def help(message: telebot.types.Message):
    text = ' <имя валюты, цену которой вы хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>. /vales'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много символов.')

        quote, base, amount = values
        total_base = CryptoConvecter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply.to(f'Неудалось выполнить команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


@bot.message_handler()
def echo_test(messsage: telebot.types.Message):
    bot.send_message(messsage.chat.id, 'hello')


bot.polling()
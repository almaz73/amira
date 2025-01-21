import telebot
# from telebot.async_telebot import AsyncTeleBot
# import asyncio

TOKEN = '7808348416:AAGgX9gNJvZL4PVTwx-faDU9DoTfEqGEyd8'
# bot = AsyncTeleBot(token=TOKEN)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print('=0=message', message)
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print('==message', message)
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)
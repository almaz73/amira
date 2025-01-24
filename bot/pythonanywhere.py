import telebot
# pip install pytelegrambotapi
import wb
import env

TOKEN = env.TELEGRAM_TOKEN
# bot = AsyncTeleBot(token=TOKEN)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['wb'])
def start(message):
    ans = wb.getWB()
    bot.send_message(message.from_user.id, ans)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)
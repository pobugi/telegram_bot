import telebot
from bashorg_parse import get_anecdote

TOKEN = '1696119213:AAFyrSrli7F-xGjAIP2LhccbCxSrIPspRjE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    content = get_anecdote()
    print(content)
    bot.send_message(message.from_user.id, content)


bot.polling()
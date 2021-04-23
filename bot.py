import telebot
from weather_api import current_weather

TOKEN = '1696119213:AAFyrSrli7F-xGjAIP2LhccbCxSrIPspRjE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Привет, пользователь!")

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Меня только что создали, могу ответить только на /start и /help")

@bot.message_handler(commands=['test'])
def test_handler(message):
    bot.send_message(message.from_user.id, message.from_user.username)


@bot.message_handler(commands=['weather'])
   
def echo(message):
    bot.send_message(message.from_user.id, current_weather(message.text))


bot.polling()
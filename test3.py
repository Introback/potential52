import telebot
from telebot import apihelper
apihelper.proxy = {'https':'socks5://127.0.0.1:9050'}

bot = telebot.TeleBot("775213554:AAE9878G2LmaEMoSavhy9J_ZE_oB0aK1SJw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message (message.chat.id, message.text)

bot.polling(none_stop = True)
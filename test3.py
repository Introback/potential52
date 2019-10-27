import telebot

bot = telebot.TeleBot("775213554:AAE9878G2LmaEMoSavhy9J_ZE_oB0aK1SJw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message (message.chat.id, message.text)

bot.polling(none_stop = True)

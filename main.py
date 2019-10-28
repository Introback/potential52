import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot("775213554:AAE9878G2LmaEMoSavhy9J_ZE_oB0aK1SJw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = ("В городе " + message.text + " сейчас " + w.get_detailed_status() + ".\n")
	answer += ("Температура сейчас в районе " + str(temp) + ".\n")

	if temp < 10:
		answer += ("Сейчас ппц как холодно, одевайся как танк!" + "\n")
	elif temp < 20:
		answer += ("Сейчас холодно, оденься потеплее." + "\n")
	else:
		answer += ("Температура норм, одевай что угодно." + "\n")

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)

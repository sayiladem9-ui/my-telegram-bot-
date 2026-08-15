import telebot

# BotFather-dən aldığın API Token-i bura yaz
TOKEN = "BURAYA_BOT_TOKENİ_YAZ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Bot uğurla işləyir 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Sən yazdın: {message.text}")

bot.polling()

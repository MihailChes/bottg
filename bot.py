from config import token
import telebot, random

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Привет!
""")
@bot.message_handler(commands=["chot", "chotnoe"])
def chotnoe(message):
    number = random.randint(1, 999)
    bot.reply_to(message, number)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
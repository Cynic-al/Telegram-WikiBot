import time
import telebot
import wikipedia

TOKEN = "1503600288:AAE8ACAjd1uGlQCwcUbpdH-gjjBTLw-w0g8"
bot = telebot.TeleBot(token=TOKEN)

def FiveOptions(e, search):
    wikioptions = list(e.options)
    for i in range(5):
        bot.send_message(search.chat.id , wikioptions[i])
        


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, nice to meet you!')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'I am a bot that searches for wiki articles based on input! To get started, simply type what you are looking for. If your search did not match what you are looking for, please add a descriptor like: Minecraft game')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(search):
    try:
        try:
            try:
                bot.send_message(search.chat.id, wikipedia.summary(search.text))
            except wikipedia.exceptions.PageError:
                bot.send_message(search.chat.id, f'Sorry, we could  not understand your search, please try again or search for a topic similar. It might help to add a descriptor like: Minecraft game ')
        except KeyError:
            bot.send_message(search.chat.id, f"Sorry, we do not accept replies, please try again.")
    except wikipedia.exceptions.DisambiguationError as e:
        bot.send_message(search.chat.id , f"Sorry, we could not understand your search, it may refer to these following topics:")
        FiveOptions(e,search)
bot.polling()
    

bot.polling()
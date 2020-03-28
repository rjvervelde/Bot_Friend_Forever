from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def start_callback(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text("You said: " + user_says)
    update.message.reply_text("Welcome to my awesome bot!")
    '''chat_id = update.message.chat_id
    bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my awesome bot!")'''

def talk(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def main():
    updater = Updater('999799466:AAEt6tJbek9P5qC1ZlHTrKmDmU34dpmjDB8')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_callback))
    dp.add_handler(CommandHandler('talk',talk))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
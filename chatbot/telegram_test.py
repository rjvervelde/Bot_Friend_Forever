from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import aiml

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def talk(bot, update):
    while True:
        message = input("Enter your message >> ")
        
        if message == "quit":
            break #useful in notebook
            # exit() # useful in actual application
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
            # star, user_response = extract_information()
            #process_response = process_user_response(user_response, star)
            # Do something with bot_response
            # syntactic parse
            # prosodic parse
            
            #print(bot_response)
    return bot_response

def main():
    updater = Updater('999799466:AAEt6tJbek9P5qC1ZlHTrKmDmU34dpmjDB8')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('talk',talk))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import aiml
from sentiment_fancy import sentiment_of_text

def set_parameters():
    kernel.setPredicate("status", "neutral")
    kernel.setPredicate("birthday", "undefined")
    kernel.setPredicate("age", "undefined")
    return

def birthday(born):
    list_string = born.split()
    year = int(list_string[-1])
    month = list_string[-2]
    day = list_string[-3]
    diff = 2020 - year
    if diff < 16:
        classs = "0"
    else:
        classs = "1"

    return f"{diff}", classs

def extract_information(user_message):
    if kernel.getPredicate("status") == "neutral":
        sentiment = sentiment_of_text(user_message)
        
        if sentiment < 0:
            kernel.setPredicate("status", "not so good")
        else:
            kernel.setPredicate("status", "good")
    
    # if kernel.getPredicate("birthday") == "undefined":
    #     kernel.setPredicate("birthday", birthday(user_message)[0])
    #     kernel.setPredicate("age", birthday(user_message)[1])
        
    return

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("simple-start.xml")
kernel.respond("load aiml")

set_parameters()

# Press CTRL-C to break this loop
while True:
    message = input("Enter your message >> ")
    
    if message == "quit":
        break #useful in notebook
        # exit() # useful in actual application
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        extract_information(message)
        bot_response = kernel.respond(message)
        
        print(bot_response)
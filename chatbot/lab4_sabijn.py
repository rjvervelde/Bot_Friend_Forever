import aiml
from sentiment_fancy import sentiment_of_text

def set_parameters():
    kernel.setPredicate("status", "neutral")
    kernel.setPredicate("age", "undefined")
    return

def extract_information(user_message):
    if kernel.getPredicate("status"):
        sentiment = sentiment_of_text(user_message)
        
        if sentiment < 0:
            kernel.setPredicate("status", "not so good")
        else:
            kernel.setPredicate("status", "good")

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
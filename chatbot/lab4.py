import aiml

def extract_information():
    if kernel.getPredicate('origin'):
        return 0, kernel.getPredicate('origin')
    elif kernel.getPredicate('destination'):
        return 1, kernel.getPredicate('destination')
    
def process_user_response(user_response, star):
    if star == 0:
        return "thanks for giving your location, which is: " + user_response
    elif star == 1:
        return "thanks for giving your destination, which is: " + user_response

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("simple-start.xml")
kernel.respond("load aiml")

# Press CTRL-C to break this loop
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
        
        print(bot_response)
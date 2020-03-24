import aiml
from API_trips import get_trip
from API_departures import get_departures, get_arrivals
from API_first_last import get_first_train, get_last_train

def check_now(response):
    if response[-4:] == '2020':
        response = response.split()[3].split()[0].rsplit(':',1)[0]
    return response

def extract_information():
    which_predicates = []
    info_per_predicate = []

    if kernel.getPredicate('origin'):
        which_predicates.append(0), info_per_predicate.append(kernel.getPredicate('origin'))
    if kernel.getPredicate('destination'):
        which_predicates.append(1), info_per_predicate.append(kernel.getPredicate('destination'))
    if kernel.getPredicate('arriving_time'):
        which_predicates.append(2), info_per_predicate.append(kernel.getPredicate('arriving_time'))
    if kernel.getPredicate('leaving_time'):
        which_predicates.append(3), info_per_predicate.append(kernel.getPredicate('leaving_time'))

    return which_predicates, info_per_predicate
    
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
        star, user_response = extract_information()
        process_response = process_user_response(user_response, star)

        print(bot_response)
        # procedure for normal advice 
        if bot_response[0:5] == "Great":
            for index, element in enumerate(star):
                if element == 0:
                    origin = user_response[index]
                elif element == 1:
                    destination = user_response[index]
                elif element == 2:
                    boolean = 'true'
                    tijd = user_response[index]
                    time = '2020-03-30T' + tijd + ':00.00Z'
                elif element == 3:
                    boolean = 'false'
                    tijd = check_now(user_response[index])
                    time = '2020-03-30T' + tijd + ':00.00Z'
            get_trip(origin, destination, time, boolean)
        
        elif bot_response[0:7] == "Leaving":
            for index, element in enumerate(star):
                if element == 0:
                    origin = user_response[index]

            get_departures(origin)

        elif bot_response[0:8] == "Arriving":
            for index, element in enumerate(star):
                if element == 0:
                    origin = user_response[index]
            
            get_arrivals(origin)
        
        elif bot_response[0:8] == 'The last':
            for index, element in enumerate(star):
                if element == 0:
                    origin = user_response[index]
                elif element == 1:
                    destination = user_response[index]
            
            boolean = 'false'
            time = '2020-03-30'
            get_last_train(origin, destination, time, boolean)

        elif bot_response[0:8] == 'The first':
            for index, element in enumerate(star):
                if element == 0:
                    origin = user_response[index]
                elif element == 1:
                    destination = user_response[index]
            
            boolean = 'false'
            time = '2020-03-30'
            get_first_train(origin, destination, time, boolean)


        

        

        
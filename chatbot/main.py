import aiml
import pandas as pd
import os
from sentiment_fancy import sentiment_of_text
from datetime import date, datetime

def set_parameters():
    kernel.setPredicate("feeling", "neutral")
    kernel.setPredicate("birthday", "everyday there is time for a party")
    kernel.setPredicate("age", "undefined")
    kernel.setPredicate("age_category", "undefined")
    kernel.setPredicate("how_many_days", "it is always youre birthday")
    
    return

def birthday(born):
    try:
        today = date.today()
        d = today.strftime("%d/%m/%Y")
        current_day, current_month, current_year = d.split("/")
        birth_day, birth_month, birth_year = born.split()[-1].split('-')
        kernel.setPredicate("birthday", f"{born.split()[-1]}")
        
        if int(birth_month) < int(current_month):
            diff = int(current_year) - int(birth_year)
        elif birth_month == current_month:
            if int(birth_day) < int(current_day):
                diff = int(current_year) - int(birth_year)
            else:
                diff = int(current_year) - int(birth_year) - 1
        else:
            diff = int(current_year) - int(birth_year) - 1

        if diff < 16:
            classs = "0"
        else:
            classs = "1"

        return f"{diff}", classs

    except:
        return f"undefined", "undefined"

def calculate_until_birthday():
    birthday = kernel.getPredicate("birthday")
    birth_day, birth_month, birth_year = birthday.split('-')

    today = datetime.now()

    delta1 = datetime(today.year, int(birth_month), int(birth_day))
    delta2 = datetime(today.year+1, int(birth_month), int(birth_day))
    days = (max(delta1, delta2) - today).days

    return f"{days}"

def extract_information(user_message):
    # sentiment analysis
    if kernel.getPredicate("feeling"):
        sentiment = sentiment_of_text(user_message)
        if sentiment < 0:
            
            kernel.setPredicate("feeling", "not so good")
        else:
            kernel.setPredicate("feeling", "good")
    
    # calculate age
    for element in user_message:
        if element == '-':
            kernel.setPredicate("age", birthday(user_message)[0])
            kernel.setPredicate("age_category", birthday(user_message)[1])
            break
    
    # how many days until you're birthday
    if user_message.lower()[-8:] == "birthday":
        kernel.setPredicate("how_many_days", calculate_until_birthday())

    return

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("simple-start.xml")
kernel.respond("load aiml")

set_parameters()

def to_txt_file(information):
    # Open the file in append & read mode ('a+')
    with open("data.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # if information is already in textfile, don't change anything
        if information in file_object.read():
            return

        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(information)
        file_object.write("\n")

# pandas can't  read an empty csv file
if os.stat("data.txt").st_size != 0:
    data_age_name = pd.read_csv("data.txt", header = None)
else:
    data_age_name = []

# Press CTRL-C to break this loop
while True:
    if len(data_age_name) > 0:
        kernel.setPredicate("name", data_age_name[0][0])
        if len(data_age_name) > 1:
            kernel.setPredicate("birthday", data_age_name[0][1])

    message = input("Enter your message >> ")

    if message == "quit":
        naam = kernel.getPredicate("name")
        bday = kernel.getPredicate("birthday")
        to_txt_file(naam)
        to_txt_file(bday)
        print(f"Bye, {naam}, see you soon!")
        break 
    else:
        extract_information(message)
        bot_response = kernel.respond(message)
        
        print(bot_response)
        


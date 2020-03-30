import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')

# Example of user input
# string = """ Hey! My name is Ellen. I am 22 years old. I am a woman.
# You can reach met at ellenbogaards@gmail.com, please send me an email if you want to contact me!"""

string = input("Enter your message >> ")

# a number between 1 and 100 will be seen as the 'age'
def extract_age(string):
    r = re.compile(r'\d{1,3}')
    ages = r.findall(string)
    return [re.sub(r'\D', '', age) for age in ages]

# format of emailadresses is recognised
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

# not really good contruction for gender,
# but if these words are in the string it will be recognised as the gender
def extract_gender(string):
    f = ['female', 'woman', 'girl', 'lady', 'mrs', 'ms']
    m = ['male', 'man', 'boy', 'sir', 'mr']
    gender = 'unkown'
    for i in m:
        if i in string:
            gender = 'male'
    for i in f:
        if i in string:
            gender = 'female'
    return gender

# names will be recognised with NLTK
def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

def save_data_in_dictionary(data):
    # the user tells its name
    if len(extract_names(string)) != 0:
        data["name"] = extract_names(string)[0]

    # the user tells its age
    if len(extract_age(string)) != 0:
        data["age"] = extract_age(string)[0]
    return data

def to_txt_file(information):
    # Open the file in append & read mode ('a+')
    with open("chatbot_data_user.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(information)

if __name__ == '__main__':
    information = ""
    if len(extract_names(string)) != 0:
        information += "The name of the user is {}.".format(extract_names(string)[0])
    if len(extract_age(string)) != 0:
        information += "The age of the user is {}.".format(extract_age(string)[0])
    to_txt_file(information)

    
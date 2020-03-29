import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')

# Example of user input
string = """ Hey! My name is Ellen. I am 22 years old. I am a woman.
You can reach met at ellenbogaards@gmail.com, please send me an email if you want to contact me!"""

# string = input("Enter your message >> ")

def extract_age(string):
    r = re.compile(r'\d{1,3}')
    ages = r.findall(string)
    return [re.sub(r'\D', '', age) for age in ages]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

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


if __name__ == '__main__':
    age = extract_age(string)
    emails = extract_email_addresses(string)
    names = extract_names(string)
    gender = extract_gender(string)
    print("The name of the user is", names[0])
    print("The user is",age[0],"years old")
    print("The e-mailadres of the user is", emails[0])
    print("The gender of the user is", gender)
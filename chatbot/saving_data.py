import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')


string = """
Hey! My name is Ellen. I am 22 years old. 
You can reach met at ellenbogaards@gmail.com, please send me an email if you want to contact me!
"""

def extract_age(string):
    r = re.compile(r'\d{1,3}')
    ages = r.findall(string)
    return [re.sub(r'\D', '', age) for age in ages]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

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
    print("The name of the user is", names[0])
    print("The user is",age[0],"years old")
    print("The e-mailadres of the user is", emails[0])
"""
Makes pie chart of tweets 
"""
 # import stuff
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer 


def load_words(filename):
    content = open(filename)
    lines = content.read().splitlines()
    content.close()
    return lines

def load_positive_words():
    return load_words("pos_words.txt")

def load_negative_words():
    return load_words("neg_words.txt")

def clean_up(word):
    lemmatizer = WordNetLemmatizer() 

    if not word.isalpha():
        print("hello")
        word = word.strip(".,!?:;")
        word = word.strip()
    
    word = word.lower()
    word = lemmatizer.lemmatize(word)
    
    return word.strip()

def sentiment_of_word(word):
    pos_words = load_positive_words()
    neg_words = load_negative_words()

    if word in pos_words and word.isalpha():
        return 1

    if word in neg_words and word.isalpha():
        return -1

    return 0

def sentiment_of_text(text):
    total_score = 0
    for word in text.split(" "):
        word = clean_up(word)
        total_score += sentiment_of_word(word)
    return total_score

# hier komt de het antwoord van de user
text = """
    prints
    """

print(sentiment_of_text(text))








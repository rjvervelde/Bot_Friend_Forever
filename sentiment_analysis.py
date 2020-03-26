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
    """ 
    Downloaded from https://www.kaggle.com/rtatman/sentiment-lexicons-for-81-languages 
    """
    return load_words("positive_words_nl.txt")

def load_negative_words():
    """ 
    Downloaded from https://www.kaggle.com/rtatman/sentiment-lexicons-for-81-languages 
    """
    return load_words("negative_words_nl.txt")

def clean_up(word):
    lemmatizer = WordNetLemmatizer() 

    if not word.isalpha():
        word = word.strip(".,!?:;")
        word = word.strip()
    
    word = word.lower()
    word = lemmatizer.lemmatize(word)
    
    return word

def sentiment_of_word(word):
    pos_words = load_positive_words()
    neg_words = load_negative_words()

    if word in pos_words:
        return 1

    if word in neg_words:
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
    precies
    """

# print(sentiment_of_text(text))







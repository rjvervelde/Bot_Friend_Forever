"""
Makes pie chart of tweets 
"""
 # import stuff
import matplotlib.pyplot as plt


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
    if word.isalpha():
        return word.lower()
    else:
        word = word.strip(".,!?:;")
        word = word.strip(" ")

        return word.lower()

def sentiment_of_word(word):
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

def classify(tweets, positives, negatives):
    """
    Classify all tweets in filename
    prints the number of tweets classified as either
    positive / negative / neutral.
    """

    # introduce variables counting amount of positive/negative/neutral words
    t_positive = 0
    t_negative = 0
    t_neutral = 0

    # checks for every tweet of the sentiment score is negative, positive or neutral
    for tweet in tweets:
        score = sentiment_of_text(tweet)
        # tweet is positive when score is higher then zero
        if score > 0:
            t_positive += 1
        # tweet is negative when score is lower then zero
        elif score < 0:
            t_negative += 1
        # tweet is neutral when score is equal to zero
        else:
            t_neutral += 1

    return t_positive, t_negative, t_neutral

# list of postive and negative words
pos_words = load_positive_words()
neg_words = load_negative_words()

# load tweets 
with open("trump.txt") as tweet_file:
       tweets = tweet_file.read().splitlines()
    
t_positive, t_negative, t_neutral = classify(tweets, pos_words, neg_words)
print("positief", t_positive)
print("negatief", t_negative)
print("neutral", t_neutral)
total = t_positive + t_negative + t_neutral
ppos = t_positive / total * 100
pneg = t_negative / total * 100
pneu = t_neutral / total * 100

# plot a pie
labels = 'Positief :)', 'Negatief :(', 'Neutraal :|'
sizes = [ppos, pneg, pneu]
exploded = [0.1, 0, 0]

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.pie(sizes, labels=labels, colors = ['g', 'r', 'w'], autopct = '%.1f%%', wedgeprops={"edgecolor":"k",'linewidth': 1, 'antialiased': True}, explode = exploded)

# zorgt dat het een rondje is anders wordt het een vage ovaal
plt.axis('equal')
plt.show()
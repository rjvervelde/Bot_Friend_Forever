from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_of_sentence(sentence):
"""
Function to calculate sentiment of sentence using vader sentiment 
"""
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 

    if sentiment_dict['compound'] >= 0.05 : 
        print(f"This sentence is positive with a score of {sentiment_dict['pos'] * 100}%")
        return 1
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print(f"This sentence is negative with a score of {sentiment_dict['neg'] * 100}%")
        return -1
  
    else : 
        print(f"This sentence is neutral with a score of {sentiment_dict['neu'] * 100}%")
        return 0

def sentiment_of_text(text):
    """
    Functino to loop through text to get sentences
    """
    total_sentiment = 0
    amount = 0
    for sentence in text.split("."):
        total_sentiment += sentiment_of_sentence(sentence)
        amount += 1
    
    return total_sentiment, amount

text = """Zeus was the first of the GODS and a very imposing figure. 
    Often referred to as the “Father of Gods and men”, he is a sky god who controls lightning (often using it as a weapon) and thunder. 
    Zeus is king of Mount Olympus, the home of Greek gods, where he rules the world and imposes his will onto gods and mortals alike.
    Zeus was the last child of the titans Cronus and RHEA, 
    and avoided being swallowed by his father (who had been told one of his children would overthrow him) 
    when Rhea sought help from URANUS and Ge. 
    Cronus had previously swallowed DEMETER, HESTIA, HERA, HADES and POSEIDON."
"""
total, amount_of_sentences = sentiment_of_text(text)

if -2 < total < 2:
    print(f'This text is neutral with of score of {abs(total / amount_of_sentences * 100)} %')
elif total <= -2:
    print(f'This text is negative with of score of {abs(total / amount_of_sentences * 100)} %')
else:
    print(f'This text is positive with of score of {abs(total / amount_of_sentences * 100)} %')
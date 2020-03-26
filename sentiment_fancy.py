from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_of_sentence(sentence):
"""
Function to calculate sentiment of sentence using vader sentiment 
"""
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 

    if sentiment_dict['compound'] >= 0.05 : 
        return 1
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        return -1
  
    else : 
        return 0

def sentiment_of_text(text):
    """
    Functino to loop through text to get sentences
    """
    total_sentiment = 0
    for sentence in text.split("."):
        total_sentiment += sentiment_of_sentence(sentence)
    
    return total_sentiment

text = """Zeus was the first of the GODS and a very imposing figure. 
    Often referred to as the “Father of Gods and men”, he is a sky god who controls lightning (often using it as a weapon) and thunder. 
    Zeus is king of Mount Olympus, the home of Greek gods, where he rules the world and imposes his will onto gods and mortals alike.
    Zeus was the last child of the titans Cronus and RHEA, 
    and avoided being swallowed by his father (who had been told one of his children would overthrow him) 
    when Rhea sought help from URANUS and Ge. 
    Cronus had previously swallowed DEMETER, HESTIA, HERA, HADES and POSEIDON."
"""
total = sentiment_of_text(text)
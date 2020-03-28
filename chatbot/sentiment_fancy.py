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
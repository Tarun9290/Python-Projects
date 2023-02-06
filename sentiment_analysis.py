#SENTIMENT ANALYSIS

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analyzer(sentence):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

sentence = "This movie was awesome! The acting was great and there were some funny scenes."
print(sentiment_analyzer(sentence))

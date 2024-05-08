from langdetect import detect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class NlpService:
  def detect_language(self, text: str) -> str:
    language = detect(text)

    return language

  def analyze_sentiment(self, text: str, *, threshold: float) -> str:
    analyzer = SentimentIntensityAnalyzer()

    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= threshold:
      return 'positive'
    
    if compound_score <= -threshold:
      return 'negative'
    
    return 'neutral'

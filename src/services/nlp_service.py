from langdetect import detect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from services.translate_service import TranslateService

translate_service = TranslateService()

class NlpService:
  def detect_language(self, text: str) -> str:
    language = detect(text)

    return language
  
  def translate_text(self, text: str, source_language: str, target_language: str) -> str:
    translated_text = translate_service.translate_text(text, source_language, target_language)

    return translated_text

  def analyze_sentiment(self, text: str, *, threshold: float) -> str:
    analyzer = SentimentIntensityAnalyzer()

    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= threshold:
      return 'positive'
    
    if compound_score <= -threshold:
      return 'negative'
    
    return 'neutral'

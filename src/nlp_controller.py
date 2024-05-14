from flask import Blueprint, jsonify, request

from services.nlp_service import NlpService

nlp_bp = Blueprint('nlp', __name__)

nlp_service = NlpService()

@nlp_bp.post('/detect-language')
def detect_language():
  text = request.json['text']

  language = nlp_service.detect_language(text)

  return jsonify({
    'language': language,
  }), 200

@nlp_bp.post('/translate-text')
def translate_text():
  text = request.json['text']
  source_language = request.json['sourceLanguage']
  target_language = request.json['targetLanguage']

  translated_text = nlp_service.translate_text(
    text,
    source_language = source_language,
    target_language = target_language,
  )

  return jsonify({
    'translatedText': translated_text,
  }), 200

@nlp_bp.post('/analyze-sentiment')
def analyze_sentiment():
  text = request.json['text']

  sentiment = nlp_service.analyze_sentiment(text, threshold = 0.2)

  return jsonify({
    'sentiment': sentiment,
  }), 200

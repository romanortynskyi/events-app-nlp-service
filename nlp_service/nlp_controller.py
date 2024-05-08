from flask import Blueprint, jsonify, request

from nlp_service import NlpService

nlp_bp = Blueprint('nlp', __name__)

nlp_service = NlpService()

@nlp_bp.post('/detect-language')
def detect_language():
  text = request.json['text']

  language = nlp_service.detect_language(text)

  return jsonify({
    'language': language,
  }), 200

@nlp_bp.post('/analyze-sentiment')
def analyze_sentiment():
  text = request.json['text']

  sentiment = nlp_service.analyze_sentiment(text, threshold = 0.2)

  return jsonify({
    'sentiment': sentiment,
  }), 200

import os
import boto3

class TranslateService:
  def __init__(self):
    access_key_id = os.getenv('TRANSLATE_ACCESS_KEY_ID')
    secret_access_key = os.getenv('TRANSLATE_SECRET_ACCESS_KEY')

    self.translate_client = boto3.client(
      'translate',
      aws_access_key_id = access_key_id,
      aws_secret_access_key = secret_access_key,
    )

  def translate_text(self, text: str, source_language: str, target_language: str) -> str:
    result = self.translate_client.translate_text(
      Text = text,
      SourceLanguageCode = source_language,
      TargetLanguageCode = target_language,
    )

    translated_text = result['TranslatedText']

    return translated_text

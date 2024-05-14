from flask import Flask
from dotenv import load_dotenv

from nlp_controller import nlp_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(nlp_bp, url_prefix='/')

if __name__ == '__main__':
  app.run(debug = True)

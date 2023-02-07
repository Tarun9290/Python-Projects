#NEWS AGGREGATOR

import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    newsapi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"
    response = requests.get(newsapi)
    news_data = json.loads(response.text)
    return render_template("index.html", articles=news_data['articles'])

if __name__ == "__main__":
    app.run(debug=True)

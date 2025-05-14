import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

YELP_API_KEY = os.environ.get("YELP_API_KEY")
YELP_API_URL = "https://api.yelp.com/v3/businesses/search"

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    price = request.args.get('price', '1')  # Yelp: 1=cheap, 2=moderate, 3=expensive, 4=very expensive
    cuisine = request.args.get('cuisine', '').strip().lower()
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    if cuisine:
        categories = cuisine
    else:
        categories = 'restaurants'
    params = {
        "location": "Cincinnati, OH",
        "categories": categories,
        "price": price,
        "limit": 10
    }
    response = requests.get(YELP_API_URL, headers=headers, params=params)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch from Yelp", "details": response.text}), 500
    data = response.json()
    return jsonify(data.get('businesses', []))

if __name__ == "__main__":
    app.run(debug=True)

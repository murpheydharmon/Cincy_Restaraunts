# Cincinnati Restaurant Recommender Backend

This is the Flask backend for the Cincinnati Restaurant Recommender app. It provides a REST API to fetch restaurant recommendations from Yelp based on price and cuisine.

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies.

## Environment Variables
- `YELP_API_KEY`: Your Yelp Fusion API key (set this in your Render dashboard or locally in a `.env` file for development).

## Running Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export YELP_API_KEY=your_yelp_api_key_here  # or use a .env file
python3 -m flask run
```

## API Endpoint
- `GET /restaurants?price=<1-4>&cuisine=<cuisine_code>`
  - Example: `/restaurants?price=2&cuisine=italian`

## Deployment
- Deploy on [Render](https://render.com/) or similar.
- Set `YELP_API_KEY` as an environment variable in your deployment settings.

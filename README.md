# Cincinnati Restaurant Recommender

A web app that recommends restaurants in Cincinnati based on price, using the Yelp Fusion API.

## Setup

### Backend
1. Go to `backend/` and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in `backend/` with this line (replace with your API key):
   ```bash
   YELP_API_KEY=your_yelp_api_key_here
   ```
3. Run the backend:
   ```bash
   flask run
   ```

### Frontend
1. Go to `frontend/` and run:
   ```bash
   npm install
   npm start
   ```

---

## Notes
- You need a Yelp Fusion API key: https://www.yelp.com/developers/documentation/v3/authentication
- The backend exposes `/restaurants?price=<1-4>` for price filtering.
- The frontend lets users pick a price range and displays recommendations.

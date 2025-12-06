# Banglore House Price Prediction

A machine learning-based web application that predicts house prices in Bangalore using Flask, scikit-learn, and an interactive frontend.

## Features

- 🏠 Real-time house price prediction
- 📊 Interactive web UI with modern design
- 🎯 Trained ML model using scikit-learn
- 🚀 Deployed on Render with Gunicorn
- 📱 Responsive design for mobile and desktop

## Project Structure

```
house_price_prediction/
├── client/                    # Frontend (HTML, CSS, JS)
│   ├── app.html              # Main page
│   ├── app.css               # Styling
│   └── app.js                # Client logic
├── server/                    # Backend (Flask API)
│   ├── server.py             # Flask app & API routes
│   ├── util.py               # Utility functions & model loading
│   ├── requirements.txt       # Server dependencies
│   └── artifacts/            # ML model & data files
│       ├── banglore_home_prices_model.pickle
│       └── columns.json
├── model/                     # Model training files
│   ├── home_price_predictor.ipynb
│   ├── bengaluru_house_prices.csv
│   └── columns.json
├── requirements.txt           # Root dependencies
├── runtime.txt               # Python version for Render
├── Procfile                  # Startup command for Render
└── README.md                 # This file
```

## Local Setup

### Prerequisites
- Python 3.10.14 or later
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/patilrutuja23/House-Price-Predictor.git
   cd House-Price-Predictor
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   cd server
   python server.py
   ```

5. **Open in browser:**
   - Navigate to `http://localhost:5000/`

## API Endpoints

### GET `/api/get_location_names`
Returns list of available locations.

**Response:**
```json
{
  "locations": ["1st Phase JP Nagar", "Rajaji Nagar", ...]
}
```

### POST `/api/predict_home_price`
Predicts home price based on input parameters.

**Parameters:**
- `total_sqft` (float): Total area in square feet
- `bhk` (int): Number of bedrooms (1-5)
- `bath` (int): Number of bathrooms (1-5)
- `location` (string): Location name

**Response:**
```json
{
  "estimated_price": 45.67
}
```

## Deployment on Render

### Prerequisites
- GitHub account with repo pushed
- Render account

### Steps

1. **Connect Repository:**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "Create +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Build & Start:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --chdir server server:app --log-file -`
   
   (Or leave blank if Render auto-detects `Procfile`)

3. **Environment Variables (if needed):**
   - No environment variables required for basic deployment

4. **Deploy:**
   - Click "Deploy Web Service"
   - Wait for build to complete
   - Visit your live URL

## Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript, jQuery
- **Backend:** Flask 2.3.3, Python 3.10
- **ML:** scikit-learn 1.4.2, NumPy 1.26.4
- **Server:** Gunicorn 21.2.0
- **Hosting:** Render

## Model Details

The ML model is a trained scikit-learn regressor that predicts house prices based on:
- **Features:** Area (sqft), BHK, Bathrooms, Location
- **Target:** Price (in Lakh rupees)
- **Model File:** `server/artifacts/banglore_home_prices_model.pickle`

## Troubleshooting

### Build fails on Render with NumPy error
- Ensure `runtime.txt` specifies Python 3.10.14
- Verify NumPy version is 1.26.4+ (has wheels for Python 3.10)

### Locations dropdown empty
- Check browser console (F12) for network errors
- Verify `/api/get_location_names` returns data
- Ensure model artifacts are loaded

### Price prediction returns error
- Verify all form fields are filled
- Check server logs on Render for detailed errors
- Ensure location name matches available options

## Development Notes

- **Local testing:** Run `python server/server.py` and visit `http://localhost:5000`
- **Frontend only:** Open `client/app.html` directly (no server required for file viewing, but API calls will fail)
- **Production:** Deployed via Render with Gunicorn

## License

MIT License - feel free to use, modify, and distribute.

## Author

[patilrutuja23](https://github.com/patilrutuja23)

---

**Happy predicting! 🎯📊**

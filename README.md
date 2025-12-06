# Banglore House Price Prediction

https://house-price-predictor-weld.vercel.app/
<br>
A machine learning-based web application that predicts house prices in Bangalore using Flask, scikit-learn, and an interactive frontend.

## Features

- 🏠 Real-time house price prediction
- 📊 Interactive web UI with modern design
- 🎯 Trained ML model using scikit-learn
- 📱 Responsive design for mobile and desktop


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


## Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript, jQuery
- **Backend:** Flask 2.3.3, Python 3.10
- **ML:** scikit-learn 1.4.2, NumPy 1.26.4


## Model Details

The ML model is a trained scikit-learn regressor that predicts house prices based on:
- **Features:** Area (sqft), BHK, Bathrooms, Location
- **Target:** Price (in Lakh rupees)
- **Model File:** `server/artifacts/banglore_home_prices_model.pickle`



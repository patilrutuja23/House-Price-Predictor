from flask import Flask, request, jsonify, render_template, send_from_directory
import util
import os

# Configure to serve static files from client folder
app = Flask(__name__, static_folder='../client', static_url_path='', template_folder='../client')

# Load artifacts on startup
try:
    print("Loading saved artifacts...")
    util.load_saved_artifacts()
    print("Artifacts loaded successfully!")
except Exception as e:
    print(f"Warning: Could not load artifacts on startup: {e}")

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# Export app for serverless platforms (Vercel, etc.)
# This is required for deployment on Vercel
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()
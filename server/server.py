from flask import Flask, request, jsonify, render_template
import util
import os
import sys

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configure to serve static files from client folder
app = Flask(__name__, 
            static_folder=os.path.join(BASE_DIR, '../client'), 
            static_url_path='', 
            template_folder=os.path.join(BASE_DIR, '../client'))

# Load artifacts on startup (with error handling)
artifacts_loaded = False
try:
    print(f"Base directory: {BASE_DIR}")
    print("Loading saved artifacts...")
    util.load_saved_artifacts()
    artifacts_loaded = True
    print("✓ Artifacts loaded successfully!")
except Exception as e:
    print(f"✗ Error loading artifacts: {e}")
    print("App will still run, but predictions may fail")

@app.route('/')
def home():
    try:
        return render_template('app.html')
    except Exception as e:
        return f"<h1>Error</h1><p>Could not load UI: {str(e)}</p>", 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'ok',
        'artifacts_loaded': artifacts_loaded
    })

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    try:
        response = jsonify({
            'locations': util.get_location_names()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(f"Error in get_location_names: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except KeyError as e:
        print(f"Missing form parameter: {e}")
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except Exception as e:
        print(f"Error in predict_home_price: {e}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Export app for serverless platforms (Vercel, etc.)
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=False, host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    def safe_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    liczba1 = safe_float(request.args.get('liczba1'))
    liczba2 = safe_float(request.args.get('liczba2'))

    suma = liczba1 + liczba2
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "liczba1": liczba1,
            "liczba2": liczba2
        }
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

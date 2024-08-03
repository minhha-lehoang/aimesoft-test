import os
import joblib
from preprocessing import preprocess_text
import sys
from flask import Flask, request, jsonify

app = Flask(__name__)
model = None


def load_model(path):
    return {
        'classifier': joblib.load(os.path.join(path, 'classifier.pkl')),
        'vectorizer': joblib.load(os.path.join(path, 'vectorizer.pkl')),
        'label_encoder': joblib.load(os.path.join(path, 'label_encoder.pkl'))
    }


def predict(text, model):
    text = preprocess_text(text)
    vectorized_text = model['vectorizer'].transform([text])
    prediction = model['classifier'].predict(vectorized_text)
    probability = model['classifier'].predict_proba(vectorized_text)
    return model['label_encoder'].inverse_transform(prediction)[0], probability.max()


@app.route('/load_model', methods=['POST'])
def load_model_route():
    global model
    data = request.json
    model_path = data['model_path']
    model = load_model(model_path)
    return jsonify({"message": "Model loaded successfully"}), 200


@app.route('/predict', methods=['POST'])
def predict_route():
    global model
    if model is None:
        return jsonify({"error": "Model not loaded"}), 400
    data = request.json
    text = data['text']
    prediction, probability = predict(text, model)
    return jsonify({"prediction": prediction, "probability": probability}), 200


if __name__ == '__main__':
    if len(sys.argv) > 1:
        model_path = sys.argv[1]
        model = load_model(model_path)
    app.run(host='0.0.0.0', port=5000)

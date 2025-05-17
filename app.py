from flask import Flask, request, jsonify
from model import generate_text

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 50)
    result = generate_text(prompt, max_length)
    return jsonify({"generated_text": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

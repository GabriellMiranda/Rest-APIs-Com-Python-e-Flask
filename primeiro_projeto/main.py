from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/<int:id>")
def person(d):
    return jsonify({'id': id, 'name': 'Gabriel', 'profession': 'Developer'})


@app.route('/som', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['values'])
        return jsonify({'som': total})
    elif request.method == 'GET':
        total = 10 + 10
        return jsonify({'som': total})


if __name__ == "__main__":
    app.run(debug=True)

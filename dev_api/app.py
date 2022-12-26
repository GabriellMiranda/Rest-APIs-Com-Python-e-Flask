from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {'id': '0',
     'nome': 'Gabriel',
     'habilidades': ['Python', 'Django']
     },
    {'id': '1',
     'nome': 'Erike',
     'habilidades': ['Python', 'Flask']
     }
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagen': 'registro excluido'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_developers():
    if request.method == 'POST':
        dados = json.loads(request.data)
        dados['id'] = len(developers)
        developers.append(dados)
        return jsonify({'status': 'sucesso', 'mensagen': 'registro inserido'})
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'rafael',
        'tarefa': 'desenvolver metodo GET',
        'status': 'concluido'
    },
    {
        'id': 1,
        'responsavel': 'gallene',
        'tarefa': 'desenvolver metodo POS',
        'status': 'pendente'
    }
]


# listar tarefas
@app.route('/tarefas/', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)


# include tarefas
@app.route('/tarefas/', methods=['POST'])
def incluir_tarefas():
    dados = json.loads(request.data)
    dados['id'] = len(tarefas)
    tarefas.append(dados)
    return jsonify({'status': 'sucesso', 'mensagen': 'registro inserido'})


# consultar tarefa
@app.route('/tarefas/<int:id>/', methods=['GET'])
def consultar_tarefas(id):
    return jsonify(tarefas[id])


# Alterar o status de uma tarefa
@app.route("/tarefas/<int:id>/<string:status>/"
           "", methods=['PUT'])
def alterar_status_tarefa(id, status):

    tarefas[id]['status'] = status
    return jsonify({'status': 'sucesso', 'mensagem': 'registro alterado'})


#Excluir tarefa
@app.route('/tarefas/<int:id>/', methods=['DELETE'])
def excluir_tarefas(id):
    tarefas.pop(id)
    return jsonify({'status': 'sucesso', 'mensagem': 'registro removido'})

if __name__ == '__main__':
    app.run(debug=True)

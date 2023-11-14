from flask import Flask, request, jsonify

app = Flask(__name__)

mensagens = []
id_counter = 1

@app.route('/enviar', methods=['POST'])
def enviar():
    global id_counter
    msg = request.json.get('mensagem')
    nome = request.json.get('nome')
    
    if msg and nome:
        mensagem = {'id': id_counter, 'nome': nome, 'mensagem': msg}
        mensagens.append(mensagem)
        id_counter += 1
        return jsonify({'status': 'Mensagem enviada'}), 200
    return jsonify({'status': 'Erro ao enviar mensagem'}), 400

@app.route('/receber', methods=['GET'])
def receber():
    id_param = request.args.get('id', default=0, type=int)
    mensagens_a_enviar = [msg for msg in mensagens if msg['id'] > id_param]
    return jsonify({'mensagens': mensagens_a_enviar})

if __name__ == '__main__':
    app.run(debug=True, port=5555)

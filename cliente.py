import requests
import os

SERVIDOR_URL = 'http://127.0.0.1:5555'
ultima_mensagem_id = 0  # Acompanhar o ID da última mensagem recebida

def enviar_mensagem():
    nome = input("Digite seu nome: ")
    msg = input("Digite sua mensagem: ")
    resposta = requests.post(f'{SERVIDOR_URL}/enviar', json={'nome': nome, 'mensagem': msg})
    print(resposta.json()['status'])

def receber_mensagens():
    global ultima_mensagem_id
    resposta = requests.get(f'{SERVIDOR_URL}/receber?id={ultima_mensagem_id}')
    mensagens = resposta.json()['mensagens']

    if mensagens:
        for msg in mensagens:
            print(f"[{msg['id']}] {msg['nome']}: {msg['mensagem']}")
        ultima_mensagem_id = mensagens[-1]['id']  # Atualizar o ID da última mensagem recebida

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    while True:
        print("1. Enviar mensagem")
        print("2. Receber mensagens")
        print("3. Sair do programa")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            enviar_mensagem()
        elif escolha == '2':
            receber_mensagens()
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")

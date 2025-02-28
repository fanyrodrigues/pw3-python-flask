# Comentário em Python
# Importando o pacote do Flask
from flask import Flask, render_template
# Não precisa informar o tipo de varíavel, a partir do valor que damos a ela, ela recebe o seu tipo
# Carregando o Flask na variável App e Mapeamento das páginas dentro da página Views
app = Flask(__name__, template_folder='views')

# Criando a rota Principal do site
#


@app.route('/')
# Criando função no Python
# View Function: função de visualização
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    # dicionario no python
    game = {'Titulo': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'}

    jogadores = ['Fany', 'eu', 'eus', 'me', 'mes']
    return render_template('games.html',
                           game=game,
                           jogadores=jogadores)


if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host="localhost", port=5000, debug=True)

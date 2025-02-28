from flask import render_template, request


def init_app(app):

    @app.route('/')
    # Criando função no Python
    # View Function: função de visualização
    def home():
        return render_template('index.html')
    jogadores = ['Fany', 'eu', 'eus', 'me', 'mim']

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # dicionario no python
        game = {'Titulo': 'CS-GO',
                'Ano': 2012,
                'Categoria': 'FPS Online'}

    
        if request.method == 'POST':
            if request.form.get('jogador'):
            
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores)

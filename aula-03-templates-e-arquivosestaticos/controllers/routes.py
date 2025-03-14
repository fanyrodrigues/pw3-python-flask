from flask import render_template, request

jogadores = ["Fantinny", "Luna", "Dan", "Kla", "Any"]
# Array de objetos
gameList = [
    {'Título': 'Stardew Valley', 'Ano': 2016, 'Categoria': 'RPG / Simulação', 'Desenvolvedor': 'ConcernedApe', 'Plataformas': 'PC, PS4, Xbox One, Switch, Mobile', 'Modo de Jogo': 'Single-player, Multiplayer'}
]

consoleList = [{'Nome': 'Stardew Valley',
'Valor': '1299.99',
'País': 'EUA'}]

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gameList[0]
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html', game=game,
    jogadores=jogadores)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == "POST":
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gameList.append({'Título': request.form.get('titulo'),
    'Categoria': request.form.get('categoria')})
        return render_template('cadgames.html', gameList=gameList)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        console = consoleList[0]
        return render_template('consoles.html',
console=console)

    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():
        if request.method == "POST":
            if request.form.get('nome') and request.form.get('valor') and request.form.get('pais'):
                consoleList.append({'Nome': request.form.get('nome'),
                                    'Valor': request.form.get('valor'),
                                    'País': request.form.get('pais')})
        return render_template('cadconsoles.html',
consoleList=consoleList)

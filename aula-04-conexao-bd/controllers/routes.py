from flask import render_template, request, redirect, url_for
from models.database import Game, db

jogadores = ["MiDna", "davi_lambari", "fanylinda", "SuaIrmã", "Iruah"]

gameList = [{'Título': 'The Legend of Zelda: Breath of the Wild',
             'Ano': 2017,
             'Categoria': 'Mundo Aberto'},
            {'Título': 'Undertale',
             'Ano': 2016,
             'Categoria': 'RPG'},
            {'Título': 'Metal Gear Rising',
             'Ano': 2013,
             'Categoria': 'Hack and Slash'}]

consoleList = [{'Nome': 'Wii U', 'Valor': '1299.99', 'País': 'Japão'},
               {'Nome': 'Xbox 360', 'Valor': '1499.99', 'País': 'EUA'}]


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
        return render_template('games.html', game=game, jogadores=jogadores, gameList=gameList)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == "POST":
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gameList.append({'Título': request.form.get('titulo'),
                                 'Ano': request.form.get('ano'),
                                 'Categoria': request.form.get('categoria')})
        return render_template('cadgames.html', gameList=gameList)

    # ✅ Rota de estoque com listagem e cadastro
    @app.route('/estoque', methods=['GET', 'POST'])
    def estoque():
        if request.method == 'POST':
            newGame = Game(
                request.form['titulo'],
                request.form['ano'],
                request.form['categoria'],
                request.form['plataforma'],
                request.form['preco']
            )
            db.session.add(newGame)
            db.session.commit()
            return redirect(url_for('estoque'))

        gamesEmEstoque = Game.query.all()
        return render_template('estoque.html', gamesEmEstoque=gamesEmEstoque)

    # ✅ Rota separada para exclusão via POST (corrigida)
    @app.route('/delete/<int:id>', methods=['POST'])
    def delete(id):
        game = Game.query.get_or_404(id)
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('estoque'))

    # ✅ Rota para edição de jogos
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        g = Game.query.get(id)
        if request.method == 'POST':
            g.titulo = request.form['titulo']
            g.ano = request.form['ano']
            g.categoria = request.form['categoria']
            g.plataforma = request.form['plataforma']
            g.preco = request.form['preco']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editgames.html', g=g)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        console = consoleList[0]
        return render_template('consoles.html', console=console, consoleList=consoleList)

    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():
        if request.method == "POST":
            if request.form.get('nome') and request.form.get('valor') and request.form.get('pais'):
                consoleList.append({'Nome': request.form.get('nome'),
                                    'Valor': request.form.get('valor'),
                                    'País': request.form.get('pais')})
        return render_template('cadconsoles.html', consoleList=consoleList)

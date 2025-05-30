from flask import render_template, request, redirect, url_for
from models.database import Game, db

jogadores = ["MiDna", "davi_lambari",
             "fanylinda", "SuaIrmã", "Iruah"]
# Array de objetos
gameList = [{'Título': 'The Legend of Zelda: Breath of the Wild',
             'Ano': 2017,
             'Categoria': 'Mundo Aberto'},
            {'Título': 'Undertale',
             'Ano': 2016,
             'Categoria': 'RPG'},
            {'Título': 'Metal Gear Rising',
             'Ano': 2013,
             'Categoria': 'Hack and Slash'}
            ]
consoleList = [{'Nome': 'Wii U',
               'Valor': '1299.99',
                'País': 'Japão'
                },
               {'Nome': 'Xbox 360',
               'Valor': '1499.99',
                'País': 'EUA'
                }
               ]


def init_app(app):

    # criando a rota principal do site

    @app.route('/')
    # criando função no python
    # view function - Função de visualização
    def home():

        return render_template('index.html',)

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Acessando o primeiro jogo da lista de jogos
        game = gameList[0]
        if request.method == 'POST':
            if request.form.get('jogador'):  # name do input
                jogadores.append(request.form.get('jogador'))

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               gameList=gameList
                               )

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == "POST":
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gameList.append({'Título': request.form.get('titulo'),
                                 'Ano': request.form.get('ano'),
                                 'Categoria': request.form.get('categoria')
                                 })
        return render_template('cadgames.html',
                               gameList=gameList)
# ROTA DO CRUD (Estoque de Jogos)

    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        if id:
            game=Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
    def estoque():
        if request.method == 'POST':
            # Cadastrando o jogo no banco:
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
        # ORM é uma técnica de programação que facilita a interação
        # entre aplicações orientadas a objetos e bancos de dados relacionais

        # A ORM que estamos usando é a SQLAlchemy
        # Método query.all é igual ao SELECT * from
        gamesEmEstoque = Game.query.all()
        return render_template('estoque.html',
                               gamesEmEstoque=gamesEmEstoque)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # Acessando o primeiro jogo da lista de jogos
        console = consoleList[0]
        return render_template('consoles.html',
                               console=console,
                               consoleList=consoleList
                               )

    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():
        if request.method == "POST":
            if request.form.get('nome') and request.form.get('valor') and request.form.get('pais'):
                consoleList.append({'Nome': request.form.get('nome'),
                                    'Valor': request.form.get('valor'),
                                    'País': request.form.get('pais')
                                    })
        return render_template('cadconsoles.html',
                               consoleList=consoleList,
                               )

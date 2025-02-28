# Comentário em Python
# Importando o pacote do Flask
from flask import Flask
from controllers import routes
# Não precisa informar o tipo de varíavel, a partir do valor que damos a ela, ela recebe o seu tipo
# Carregando o Flask na variável App e Mapeamento das páginas dentro da página Views
app = Flask(__name__, template_folder='views')

# Criando a rota Principal do site
#
routes.init_app(app)


if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host="localhost", port=5000, debug=True)

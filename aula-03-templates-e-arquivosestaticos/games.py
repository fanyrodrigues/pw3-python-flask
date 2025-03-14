#Importando o pacote do frask
from flask import Flask
#carregando o frask na  variável app, não precisa informar o tipo de variável
#dois underline
app = Flask(__name__)
@app.route ('/games')
# criando função
def games():
    return '<h1> Seja bem vindo a página de games !! <3 <br>  </h1>'

if __name__ ==  '__main__':
#nome = "Fany"
#numero = 12 debug => decoração, true é ativado. Ele avisa os erro. Rodando o servidor no localhost, porta 5000. POde ser executado no terminal : python app.py

 app.run(host='localhost', port=5000, debug=True ) 
 
 #Rota 5 www.site, com ('/') <= principal
# www.site.com/produtos (/produtos)
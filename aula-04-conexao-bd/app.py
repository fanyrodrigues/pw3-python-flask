from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()  # Isso aqui é ESSENCIAL para usar pymysql como MySQLdb

from controllers import routes
from models.database import db

app = Flask(__name__, template_folder='views')

routes.init_app(app)

DB_NAME = 'games'

app.config['DATABASE_NAME'] = DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root@localhost/{DB_NAME}'

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados {DB_NAME} está criado!")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
    
    db.init_app(app)
    
    with app.test_request_context():
        db.create_all()
    
    app.run(host='localhost', port=5000, debug=True)

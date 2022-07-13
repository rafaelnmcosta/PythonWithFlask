from cgitb import html
from flask import Flask


# instância da classe flask
app = Flask(__name__)

#Rotas do aplicativo com decorator
@app.route("/")
def index():
    return 'Hello, world'

#Checando se o usuário está acessando o programa principal
if __name__ == '__main__':
    app.run()

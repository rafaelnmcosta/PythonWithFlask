from cgitb import html
import os

from aiohttp import request
from werkzeug.utils import secure_filename
from flask import Flask, render_template

# instância da classe flask
app = Flask(__name__, template_folder='../template')

directory = os.path.join(os.getcwd(), 'upload')

# Rotas do aplicativo com decorator
@app.route("/")
def index():
    return render_template('index.html')


# Rota que faz upload da imagem
@app.route("/upload", methods=['POST'])
def uploaded():
    file = request.files['imagem']
    savePath = os.path.join(directory, secure_filename(file.filename))
    file.save(savePath)
    return 'uploded'


# Checando se o usuário está acessando o programa principal
if __name__ == '__main__':
    app.run(debug=True)

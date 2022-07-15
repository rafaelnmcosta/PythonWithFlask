from cgitb import html
from distutils.command.upload import upload
import os

from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

# instância da classe flask
app = Flask(__name__, template_folder='../template')

UPLOAD_FOLDER = os.path.join(os.getcwd('upload'), 'upload')

# Rotas do aplicativo com decorator
@app.route("/")
def index():
    return render_template('index.html')


# Rota que faz upload da imagem
@app.route("/upload", methods=['POST'])
def uploaded():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER)
    file.save(savePath)
    return 'uploded'


# Checando se o usuário está acessando o programa principal
if __name__ == '__main__':
    app.run(debug=True)

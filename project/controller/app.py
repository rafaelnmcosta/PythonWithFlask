
import os

from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

# instância da classe flask
app = Flask(__name__, template_folder='../template')

UPLOAD_FOLDER = '../upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rotas do aplicativo com decorator
@app.route("/")
def index():
    return render_template('index.html')


# Rota que faz upload da imagem
@app.route("/upload", methods=['GET','POST'])
def uploaded():
    file = request.files['imagem']
    filename = secure_filename(file.filename)
    savePath = file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file.save(savePath)
    return 'uploded'


# Checando se o usuário está acessando o programa principal
if __name__ == '__main__':
    app.run(debug=True)

import os
from attr import attrs
import pandas as pd
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, send_file

# instância da classe flask
app = Flask(__name__, template_folder='../template')

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rotas do aplicativo com decorator


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template('index.html')


@app.route('/produto', methods=['GET', 'POST'])
def produto():
    NameList = []
    product = request.form['product']
    print(product)
    url = 'https://www.amazon.com.br/s?k='
    response = requests.get(url+product)
    print(response)
    content = response.content
    amazon = BeautifulSoup(content, 'html.parser')
    offers = amazon.find('div', attrs={
                         's-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_5'})
    name = offers.find(
        'h2', attrs={'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
    price = offers.find('span', attrs={'a-offscreen'})

    print(name.text, price.text)
    

    #title = offers.find('h2', attrs={'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
    # offers.prettify
    return render_template('produto.html', product=product)


# Rota que faz upload da imagem
"""
@app.route("/upload", methods=['GET','POST'])
def uploaded():
    file = request.files['imagem']
    filename = secure_filename(file.filename)
    savePath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(savePath)
    return render_template("index.html",filename = filename)
"""
# Checando se o usuário está acessando o programa principal
if __name__ == '__main__':
    app.run(debug=True)

from collections import namedtuple
from os import link
from turtle import title
import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_file

# instância da classe flask
app = Flask(__name__, template_folder='../template')

#UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rotas do aplicativo com decorator

# if span = ui-search-price__discount append.list


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template('index.html')


@app.route('/produto', methods=['GET', 'POST'])
def produto():
    NameList = []
    product = request.form['product']
    print(product)
    url = 'https://lista.mercadolivre.com.br/'
    response = requests.get(url+product)
    print(response)
    content = response.content
    mercadoLivre = BeautifulSoup(content, 'html.parser')
    offers = mercadoLivre.find_all(
        'div', attrs={'class': 'ui-search-result__wrapper'})

    for offer in offers:
        links = offer.find('a', attrs={'class': 'ui-search-link'})
        price = offer.find('span', attrs={'class': 'price-tag-amount'})
        name = offer.find('h2', attrs={'ui-search-item__title'})
        discount = offer.find(
            'span', attrs={'ui-search-price__second-line__label'})
        if (discount):
            NameList.append(
                [name.text, price.text, discount.text, links['href']])

    productList = pd.DataFrame(data=NameList, columns=[
                               'name', 'price', 'discount', 'links'])
    return render_template('produto.html',tables=[productList.to_html(classes='data', header=True)])

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

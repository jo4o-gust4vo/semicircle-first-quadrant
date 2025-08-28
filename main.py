from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
#from views import *

app = Flask(__name__)

@app.route('/')
def homepage():

    return  render_template('homepage.html')


@app.route('/process', methods=['POST'])
def processo():
    valorDoInput = request.form['numero']



    # Cria uma figura e um conjunto de eixos
    fig, ax = plt.subplots(figsize=(6, 6))

    # Define os limites para os eixos x e y de 0 a 50
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)

    # --- Adicionando o setor circular no primeiro quadrante ---
    # O centro do setor será na origem (0,0) para que ele preencha o quadrante
    center_x = 0
    center_y = 0

    # Raio do setor (tamanho suficiente para ser visível no gráfico)
    radius = int(valorDoInput)

    # Define os ângulos para o primeiro quadrante (0 a 90 graus)
    start_angle = 0
    end_angle = 90

    # Cria o patch do setor circular
    wedge = mpatches.Wedge((center_x, center_y), radius, start_angle, end_angle, color='lightgreen', alpha=0.8)

    # Adiciona o setor circular aos eixos
    ax.add_patch(wedge)

    # Adiciona um título para clareza
    ax.set_title("Eixos X e Y com Setor Circular no Primeiro Quadrante")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    # Garante que a proporção dos eixos seja igual para que o setor pareça circular
    ax.set_aspect('equal', adjustable='box')
    plt.savefig(r'D:\Documentos\Estudos\Faculdade\Sétimo semestre\COMPUTAÇÃO GRÁFICA\PLOT CICLE\static\imagem\circulo.png')
  

    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()
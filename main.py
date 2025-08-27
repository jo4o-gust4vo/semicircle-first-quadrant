from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import matplotlib.pyplot as plt
#from views import *

app = Flask(__name__)

@app.route('/')
def homepage():

    return  render_template('homepage.html')


@app.route('/process', methods=['POST'])
def processo():
    valorDoInput = request.form['numero']

    circle = plt.Circle((int(valorDoInput), int(valorDoInput)), int(valorDoInput), fill=False)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Add the circle to the axis
    ax.add_patch(circle)

    # Get the center and radius of the circle
    center = circle.center
    radius = circle.radius

    # Draw a line from the center to the edge to represent the radius
    ax.plot([center[0], center[0] + radius], [center[1], center[1]], 'r--', lw=1)

    # Add a text annotation for the radius value
    ax.text(center[0] + radius/2, center[1], f'Raio: {radius} cm', ha='center', va='bottom', color='green')

    # Set axis limits and show the plot
    #ax.set_xlim([0, int(valorDoInput)])
    #ax.set_ylim([0, int(valorDoInput)])

    plt.axis('equal')  # To ensure the aspect ratio is maintained
    plt.savefig(r'D:\Documentos\Estudos\Faculdade\Sétimo semestre\COMPUTAÇÃO GRÁFICA\PLOT CICLE\static\imagem\circulo.png')
  

    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()
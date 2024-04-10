from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def euler_method(x0, y0, xn, h):
    # Inicialización de listas para almacenar los valores de x, y
    x_vals = [x0]
    y_vals = [y0]

    # Número de subintervalos
    N = int((xn - x0) / h)

    # Iteración del método de Euler
    for _ in range(N):
        y_prime = x_vals[-1] - y_vals[-1]  # y'' = x - y
        y_new = y_vals[-1] + h * y_prime  # Método de Euler para y
        x_vals.append(x_vals[-1] + h)
        y_vals.append(y_new)

    return x_vals, y_vals

def plot_graph(x_vals, y_vals):
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='Solución por Euler')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.savefig('static/plot.png')  # Guardar la gráfica como imagen en la carpeta static

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        x0 = float(request.form['x0'])
        y0 = float(request.form['y0'])
        xn = float(request.form['xn'])
        h = float(request.form['h'])

        # Resolver utilizando el método de Euler
        x_vals, y_vals = euler_method(x0, y0, xn, h)
        plot_graph(x_vals, y_vals)

        # Renderizar la plantilla HTML con la tabla y la imagen
        return render_template('results.html', x_vals=x_vals, y_vals=y_vals)

    # Renderizar el formulario si no se ha enviado ningún dato
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

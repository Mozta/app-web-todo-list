from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    tasks = [
        {
            'id': 1,
            'name': 'Tomar la clase',
            'check': False
        },
        {
            'id': 2,
            'name': 'Hacer la tarea',
            'check': False
        },
        {
            'id': 3,
            'name': 'Crear mi aplicación web de tareas',
            'check': False
        },
        {
            'id': 4,
            'name': 'Crear mi aplicación web de tareas',
            'check': False
        },
    ]

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
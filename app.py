from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/page/<name>')
def page(name):
    with open(f'{name}.html', 'rb') as f:
        return f.read()


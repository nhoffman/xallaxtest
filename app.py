from flask import Flask, render_template, request

import dice
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/attack')
def attack():
    command = request.args.get('roll')
    modifier = int(request.args.get('modifier', '0'))

    name = request.args.get("name")
    car = request.args.get("cars")
    
    if command == None:
        message = 'There was no command, try again.'
    else:
        rolled = dice.roll_attack(command)
        message = f'{rolled}+{modifier} = {rolled + modifier}'
        print(message)
    
    return render_template(
        'attack.html',
        message=message,
        name=name,
        car=car)



@app.route('/page/<name>')
def page(name):
    """This route provides a way to display pre-rendered html files. '/page/<name>'
    serves the contents of a file named "<name>.html"

    """
    with open(f'{name}.html', 'rb') as f:
        return f.read()

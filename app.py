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
    command = request.args.get('command')
    
    # command = '10d6+5'
    if command == None:
        message = 'There was no command, try again.'
    else:
        command = command.replace('plus', '+')
        rolled, modifier = dice.roll_attack(command)
        message = f'{rolled}+{modifier} = {rolled + modifier}'
        print(message)
    
    return render_template(
        'attack.html',
        message=message)



@app.route('/page/<name>')
def page(name):
    """This route provides a way to display pre-rendered html files. '/page/<name>'
    serves the contents of a file named "<name>.html"

    """
    with open(f'{name}.html', 'rb') as f:
        return f.read()

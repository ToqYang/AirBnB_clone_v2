#!/usr/bin/python3
""" Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Hello World in Flask """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text="C"):
    """ Print C<text> """
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    """ Print Python """
    text = text.replace('_', ' ')

    return "Python " + text


if __name__ == "__main__":
    """ Entry point """
    app.run(host='0.0.0.0', port=5000, debug=False)

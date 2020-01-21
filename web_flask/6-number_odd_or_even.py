#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ Is it a number? """
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def index(n):
    """ Number template """
    return render_template('5-number.html', n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def odd_even(n):
    """ Is a odd or even number """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    """ Entry point """
    app.run(host='0.0.0.0', port=5000, debug=False)

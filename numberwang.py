#!/usr/bin/env python3

import random

from flask import Flask

app = Flask('numberwang')

@app.route('/')
@app.route('/<number>')
def index(number=None):
    try:
        if number == 'threeve':
            number = 4

        if numberwang(int(number)):
            return "That's numberwang!"
        else:
            return random.choice(['Nope', 'No...', '...'])
    except:
        return 'Usage: GET /[number]'


def numberwang(number):
    return random.random() < 0.25


if __name__ == '__main__':
    app.run()

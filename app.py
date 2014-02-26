#!/usr/bin/env python
import os

from flask import Flask
from matches import ConfigReader
app = Flask(__name__)

@app.route('/n_matches')
def n_matches():
    return str(ConfigReader(open("config.yml").read()).n_matches())


@app.route('/current_match')
def current_match():
    return str(ConfigReader(open("config.yml").read()).current_match())


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

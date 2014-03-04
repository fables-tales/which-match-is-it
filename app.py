#!/usr/bin/env python
import os
from flask import Flask
import json
from srcomp.matches import MatchSchedule

CONFIG_FNAME = os.path.join(os.path.dirname(__file__),
                            "config.yml")

app = Flask(__name__)

def get_schedule():
    return MatchSchedule(CONFIG_FNAME)

@app.route('/n_matches')
def n_matches():
    return str(get_schedule().n_matches())


@app.route('/current_match_number')
def current_match():
    return str(get_schedule().current_match())


def read_match_number(match_number):
    if match_number != -1:
        cm = get_schedule()
        return json.dumps(
            {
                "arena_0": cm.whos_in(match_number, "arena_0"),
                "arena_1": cm.whos_in(match_number, "arena_1")
            }
        )
    else:
        return json.dumps({})

def current_match_number():
    return int(get_schedule().current_match())

@app.route('/who/<match_number>')
def who(match_number):
    return read_match_number(int(match_number))

@app.route("/current_match_teams")
def current():
    return read_match_number(current_match_number())


@app.route('/next_match_teams')
def next():
    return read_match_number(current_match_number()+1)

@app.route('/match_after_next_teams')
def after_next():
    return read_match_number(current_match_number()+2)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5112))
    app.run(host='0.0.0.0', port=port)

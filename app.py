#!/usr/bin/env python
import os
from flask import Flask, jsonify, json
from srcomp import SRComp

ROOTDIR = os.path.dirname(__file__)

app = Flask(__name__)

def get_comp():
    return SRComp(ROOTDIR)

def match_json_info(match):
    return {
        "number": match.num,
        "arena": match.arena,
        "teams": match.teams,
        "start_time": match.start_time.isoformat(),
        "end_time": match.end_time.isoformat(),
    }

@app.route("/matches/<arena>/<int:match_number>")
def match_info(arena, match_number):
    "Get information about the given match number"
    comp = get_comp()

    if match_number not in comp.schedule.matches:
        return jsonify(error=True,msg="Invalid match number"), 404
    match = comp.schedule.matches[match_number]

    if arena not in match:
        return jsonify(error=True,msg="Invalid arena"), 404
    match = match[arena]

    return jsonify(**match_json_info(match))

@app.route("/matches/<arena>/<int:match_number_min>-<int:match_number_max>")
def match_info_range(arena, match_number_min, match_number_max):
    "Get information about the given range of matches"
    comp = get_comp()
    resp = {}

    for match_n in range(match_number_min, match_number_max+1):
        if match_n not in comp.schedule.matches:
            "Skip matches that don't exist"
            continue

        resp[match_n] = match_json_info(comp.schedule.matches[match_n][arena])

    return json.dumps(resp)

@app.route("/matches/<arena>/current")
def current_match_info(arena):
    comp = get_comp()
    current = comp.schedule.current_match()

    if current is None:
        return jsonify(number=None, msg="No current match")

    if arena not in current:
        return jsonify(error=True,msg="Invalid arena"), 404
    match = current[arena]

    return jsonify(**match_json_info(match))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5112))
    app.run(host='0.0.0.0', port=port)

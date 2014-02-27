#!/usr/bin/env python
import yaml
import sys

class CurrentMatcher:
    def __init__(self, match_schedule):
        self.matches = yaml.load(match_schedule)["matches"]

    def whos_in(self, match_number, arena_id):
        return self.matches[match_number][arena_id]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage is ./who.py <match_number>"
    else:
        cm = CurrentMatcher(open("config.yml").read())
        match_number = int(sys.argv[1])
        print "Teams in arena 0:", cm.whos_in(match_number, "arena_0")
        print "Teams in arena 1:", cm.whos_in(match_number, "arena_1")

#!/usr/bin/env python
from srcomp.matches import MatchSchedule
import sys

if len(sys.argv) != 2:
    print "Usage is ./who.py <match_number>"
else:
    cm = MatchSchedule(open("config.yml").read())
    match_number = int(sys.argv[1])
    print "Teams in arena 0:", cm.whos_in(match_number, "arena_0")
    print "Teams in arena 1:", cm.whos_in(match_number, "arena_1")

#!/usr/bin/env python
import os
from srcomp.matches import MatchSchedule
import sys

CONFIG_FNAME = os.path.join(os.path.dirname(__file__),
                            "config.yml")

if len(sys.argv) != 2:
    print "Usage is ./who.py <match_number>"
    exit(1)

cm = MatchSchedule(CONFIG_FNAME)
match_number = int(sys.argv[1])
print "Teams in arena 0:", cm.matches[match_number]["arena_0"].teams
print "Teams in arena 1:", cm.matches[match_number]["arena_1"].teams

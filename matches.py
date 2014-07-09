import os
from srcomp.matches import MatchSchedule

CONFIG_FNAME = os.path.join(os.path.dirname(__file__),
                            "config.yml")

sched = MatchSchedule(CONFIG_FNAME)

print "total match period:", sched.n_matches()
print "current match is:", sched.current_match()

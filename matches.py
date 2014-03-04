from srcomp.matches import MatchSchedule

print "total match period:", MatchSchedule(open("config.yml").read()).n_matches()
print "current match is:", MatchSchedule(open("config.yml").read()).current_match()

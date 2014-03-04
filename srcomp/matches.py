"Match schedule library"
from collections import namedtuple
import datetime
import time
import yaml

try:
    from yaml import CLoader as YAML_Loader
except ImportError:
    from yaml import Loader as YAML_Loader

MatchPeriod = namedtuple("MatchPeriod",
                         ["start_time","end_time"])

class MatchSchedule(object):
    def __init__(self, config_fname):
        with open(config_fname, "r") as f:
            y = yaml.load(f.read(), Loader = YAML_Loader)

        self.match_periods = []
        for e in y["match_sets"]:
            self.match_periods.append(MatchPeriod(e["start_time"],
                                                 e["end_time"]))

        self.match_period = y["match_period_length_seconds"]
        self.current_delay = y["current_delay"]
        self.matches = y["matches"]

    def n_matches(self):
        total = 0
        for period in self.match_periods:
            total += self.matches_in_period(period)

        return total

    def current_match(self):
        t = datetime.datetime.now() - datetime.timedelta(0, self.current_delay)
        i = 0
        match = self.match_periods[i]
        while t > match.end_time:
            i += 1
            match = self.match_periods[i]

        if t < match.start_time:
            return -1
        else:
            total = 0
            for j in xrange(0, i):
                match = self.match_periods[j]
                total += self.matches_in_period(match)

            total += self.matches_in_period(MatchPeriod(self.match_periods[i].start_time,
                                                        t))

            return total

    def matches_in_period(self, period):
        return (period.end_time - period.start_time).seconds/self.match_period

    def whos_in(self, match_number, arena_id):
        return self.matches[match_number][arena_id]

"Match schedule library"
import datetime
import time
import yaml

class MatchSchedule(object):
    def __init__(self, text):
        self.loaded_data = yaml.load(text)
        self.match_period = self.loaded_data["match_period_length_seconds"]

    def n_matches(self):
        total = 0
        for match in self.loaded_data["match_sets"]:
            total += self.matches_in_period(match)

        return total

    def current_match(self):
        t = datetime.datetime.now() - datetime.timedelta(0, self.loaded_data["current_delay"])
        i = 0
        match = self.loaded_data["match_sets"][i]
        while t > match["end_time"]:
            i += 1
            match = self.loaded_data["match_sets"][i]

        if t < match["start_time"]:
            return -1
        else:
            total = 0
            for j in xrange(0, i):
                match = self.loaded_data["match_sets"][j]
                total += self.matches_in_period(match)

            total += self.matches_in_period(
                {
                    "start_time": self.loaded_data["match_sets"][i]["start_time"],
                    "end_time": t
                }
            )

            return total

    def matches_in_period(self, match):
        return (match["end_time"] - match["start_time"]).seconds/self.match_period

    def whos_in(self, match_number, arena_id):
        return self.loaded_data["matches"][match_number][arena_id]

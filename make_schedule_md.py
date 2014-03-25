import yaml
import datetime

def match_sets():
    return yaml.load(open("config.yml"))["match_sets"]

def match_lines():
    return [x for x in open("54_with_names.txt").read().split("\n") if len(x.strip()) > 0 and x.strip()[0] != "#"]

def five_minutes():
    return datetime.timedelta(0, 300)

def day_index(set):
    if set == 0:
        return "Day 1 "
    else:
        return "Day 2 "

if __name__ == "__main__":
    current_time = match_sets()[0]["start_time"]
    current_set = 0
    match_index = 0
    with open("schedule.md", "w") as fp:
        fp.write("| Time | A0C0 | A0C1 | A0C2 | A0C3 | A1C0 | A1C1 | A1C2 | A1C3 |\n")
        fp.write("|:----:| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |\n")
        while current_time < match_sets()[-1]["end_time"]:
            match = match_lines()[match_index]

            fp.write("| %s at %02d:%02d | %s |" % (day_index(current_set), current_time.hour, current_time.minute, match))
            fp.write("\n")
            match_index += 1
            current_time += five_minutes()

            if match_index >= len(match_lines()):
                break

            if current_time >= match_sets()[current_set]["end_time"]:
                current_set += 1
                current_time = match_sets()[current_set]["start_time"]

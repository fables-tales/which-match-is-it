#SRobo what match are we in tool

##Command line

run `python matches.py`

##Web

run `pip install flask`
then run `python app.py`

it's got **endpoints**

```
/n_matches

the number of matches

/current_match_number

the current match number
```


##But what if there's a delay?

config.yml has a current delay value, which is seconds. Set it based on how
behind we are, watch get dealt with disappear.

**CAN YOU BELIEVE IT'S THAT SIMPLE**

#I'm sorry it got more complicated

Now it knows which matches people are in too

#SRobo who is in this match tool

##Command line

run `./who.py <match_number>`

##Web

run `pip install flask` then run `python app.py`

it's got **endpoints**

```
/who/<match_number>

shows who is in the match with match number (zero indexed)

/current_match_teams

shows who is in the current match

/next_match_teams

shows who is in the next match

/match_after_next_teams

shows who is in the match after the next match
```

All responses are YAML

##CONFIGURING

![Configuring is hard](http://4.bp.blogspot.com/-fYJrkNWec08/T9EYOmNGPNI/AAAAAAAAC04/UtdRRM8a3hc/s640/cat-fat-dancing-cat-gif.gif)

Give it a config.yml that looks like the one in this repository but with
more matches because there will be more matches

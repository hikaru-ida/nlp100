import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(",", "")
s = s.replace(".", "")
ls = [ len(token) for token in s.split() ]
print(ls)

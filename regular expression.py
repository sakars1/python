import re

val = "I was going to the College."
if re.match('.*College.$',val):
    print("True")
else:
    print("False")


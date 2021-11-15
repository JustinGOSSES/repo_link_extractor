print("testing if this python script ran by a print statement")

import markdown
import re

f = open('myfile.txt', 'r') 
f.read() 

p = re.compile(https:\/\/github.com\/)\w+(\/)\w+

matched = p.match(f)

print("matched",matched)

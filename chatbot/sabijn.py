import re

txt = "The rain in Spain"
x = re.search(".*birthday.*", txt)

print(x)
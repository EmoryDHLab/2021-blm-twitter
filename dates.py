import csv
import sys
import re


with open(sys.argv[1]) as make_dates:
    make_dates_reader = make_dates.read() + "\n"

match = re.findall("20\d\d-\d\d-\d\d", make_dates_reader)
print(match)

with open(sys.argv[2], "w") as write_dates:
    for row in match:
        write_dates.write(row + "\n")
write_dates.close()
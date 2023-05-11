#!/usr/bin/env python3
"""Parse a CSV manually and print out a row selected by the user."""

with open("cars.csv") as f:
    lines = f.readlines()

nmbr_of_lines = len(lines)

print(f"There are {nmbr_of_lines} lines in the csv")
n = int(input(f"Enter an inclusive number, 1 to {nmbr_of_lines-2}: "))

header = lines[0].strip().split(",")
row = lines[n].strip().split(",")

# create a dictionary with the header as keys and the row as values
car = dict(zip(header, row))
model = car["Car"]
country = "the US" if car["Origin"] == "US" else car["Origin"]

hp = float(car["Horsepower"])
kw = hp * 746 / 1000

output = f"""
HEADER
{header}
LINE {n}
{row}
The {model} made in {country} generates {hp} HP, or {kw} KW of power.
"""

print(output)

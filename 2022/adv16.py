# Setup
import re
file = open('adv16.txt', 'r')
lines = [l.strip() for l in file.readlines()]

valves = {}
valves_worth_opening = []

for line in lines:
    parts = line.split(' ')
    _ ,rate = parts[4].split('=')
    rate = int(rate.replace(';', ''))
    ways = [valve.replace(',', '') for valve in parts[9:]]
    valves[parts[1]] = { 'rate': rate, 'ways': ways }
    
    if rate > 0:
        valves_worth_opening.append(parts[1])

print(valves_worth_opening)
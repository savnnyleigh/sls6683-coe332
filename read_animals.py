
import json
import random

with open('animals.json', 'r') as f:
	animals = json.load(f)

print(random.choice(animals))


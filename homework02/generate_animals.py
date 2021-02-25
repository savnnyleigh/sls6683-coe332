
#!/usr/bin/env python3

import sys
import petname
import random
import json

head_list=['snake','bull', 'lion', 'raven', 'bunny']

animals = []

for x in range(20):
	animal = {
		"head": random.choice(head_list),
	 	"body": random.choice(petname.names) + "-" + random.choice(petname.names),
	 	"arms": (random.randint(1,5))*2,
	 	"legs": (random.randint(1,4))*3, 
	 	"tail": 1
	}

	tailc = animal.get('arms') + animal.get('legs')
	animal['tail'] = tailc
	animals.append(animal)


with open(sys.argv[1], 'w') as out:
	json.dump(animals, out, indent = 2)




import json
import random

def breed(parents):
	Nanimal = {

        	        "head": random.choice(parents)['head'],
                	"body": random.choice(parents)['body'],
        	     	"arms": random.choice(parents)['arms'],
                	"legs": random.choice(parents)['legs'],
                	"tail": 1
        	}

	tailc = Nanimal.get('arms') + Nanimal.get('legs')
	Nanimal['tail'] = tailc
	
	return Nanimal

def main():

	with open('animals.json', 'r') as f:
		animals = json.load(f)

	parent1 = random.choice(animals)
	parent2 = random.choice(animals)

	parents = [parent1, parent2]

	newanimal = breed(parents)

	print("Parent one is : ", parent1)
	print("Parent two is : ", parent2)
	
	print("New breed is : ", newanimal)

if __name__ == "__main__":
    main()

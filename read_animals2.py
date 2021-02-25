
import json
import random

def breed(parent1, parent2):
	
	parents = [parent1, parent2]

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

	animal1 = random.choice(animals)
	animal2 = random.choice(animals)
	
	newanimal = breed(animal1,animal2)

	print("Parent one is : ", animal1)
	print("Parent two is : ", animal2)
		
	print("New breed is : ", newanimal)

if __name__ == "__main__":
    main()

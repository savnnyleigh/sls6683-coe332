# Containers and Repositories of Dr. Moreau

This program builds on previous homework01, where we generated random animals. Here we are 'breeding' two parents together to see an outcome of their offspring. There is also a unit test to test the validity of the breed function. 

## Installation

Pull scripts from GitHub [https://github.com/savnnyleigh/sls6683-coe332/tree/main/homework02]
```bash
git pull https://github.com/savnnyleigh/sls6683-coe332/tree/main/homework02
```

## Run Scripts Directly
This can be done once the scripts are pulled. The result of read_animals2.py will display two random parents and a resulting bred animal. Even if the parents are the same in multiple repetitions, the animal bred may be different every time, as the program randomly selects which parent's characteristic to adopt from head, body, arms, legs, and tails.

```bash
python3 generate_animals.py

python3 read_animals2.py 
```

## Dockerfile

Once Dockerfile and the other files mentioned are downloaded, run the command below.

```bash
docker build -t savnnyleigh/homework02:1.0 .
```

## Scripts inside a Container
Once inside the container, the scripts can be run interactively or non-interactively as shown below

### Interactively
```bash
docker run --rm -it username/json-parser:1.0 /bin/bash

ls /code # check that both generate_animals.py and read_animals.py are there

cd /home # go back to the home folder

generate_animals.py test.json # runs generate_animals.py and creates test.json

read_animals2.py test.json #uses test json to execute read_animals2.py

```

### Non-Interactively
In this method we use commands from the isp server rather than from inside the container
```bash
mkdir test # holds the files created from the test we are about to run

cd test # enter the test folder

docker run --rm -v $PWD:/data -u $(id -u):$(id -g) savnnyleigh/homework02:1.0 generate_animals.py /data/animals.json

ls -l # this should show you the creation of animals.json

docker run --rm -v $PWD:/data username/json-parser:1.0 read_animals2.py /data/animals.json # runs read_animals2.py with animals.json we created

```

## Unit Test
This unit test will give us the ability to check where things can be improved in the breed function. To run the unit test you can change the animal characteristics. For the purpose of this unit test both parents are the same so we can predict what characteristics the child will have. I test to make sure the head, body, arms, legs, and tail are correct, as well as the type our breed function displays. 

```bash
vim test_read_animals.py # change animal characteristics you would like to test

python3 test_read_animals.py # run test_read_animals.py if it fails adjust function

```


import redis
import json
from datetime import datetime
from flask import Flask, jsonify
from jsonRead import data

app = Flask(__name__)

def get_data():
	with open("animals.json", "r") as json_file:
        	user_data = json.load(json_file)
	return user_data

rd = redis.StrictRedis(host='redis', port=6409, db=0)
rd.set('k1', json.dumps(get_data()))

#query a range of dates
@app.route('/animals/created_on/<string:s_date>/<string:e_date>', methods = ['GET'])
def get_animals(s_date,e_date):
	test = get_data()
	animals_r = data['animals']
	list1 = []
	start = datetime.strptime(s_date, '%Y-%m-%d')
	end = datetime.strptime(e_date, '%Y-%m-%d')
	for animal in animals:
		date = datetime.strptime(animal['created_on'], '%Y-%m-%d')
		if ((date>=start) and (date<=end)):
			list1.append(animal)
	return jsonify({'animals in range': list1})

#selects a particular creature by its unique identifier
@app.route('/animals/sel/<string:sel_uid>', methods = ['GET'])
def sel_animals_uuid(sel_uid):
	test = get_data()
	animals_s = data['animals']
	for animal in animals_s:
		if (animal['uid'] == sel_uid):
			return jsonify ({'animal':animal})
		else :	
        		return jsonify ({'animal': 'animal does not exist'})

#modifying an animal based on uuid, chosen modification is to add 2 tails
@app.route('/animals/mod/<string:sel_uid>', methods = ['PUT'])
def mod_animals_uuid(sel_uid):
	test = get_data()
	animals_m = data['animals']
	for animal in animals_m:
                if (animal['uid'] == sel_uid):
			tail = animal['tail']
			animal['tail'] = tail + 2
                        return jsonify ({'modified animal':animal})
        	else :
                	return jsonify ({'animal': 'animal does not exist'})

#deletes a selection of animals by a date ranges
@app.route('/animals/del/<string:s_date>/<string:e_date>', methods = ['GET'])
def del_animals(s_date,e_date):
	test = get_data()
	animals_d = data['animals']
	list2 = []
        start = datetime.strptime(s_date, '%Y-%m-%d')
        end = datetime.strptime(e_date, '%Y-%m-%d')
	for animal in animals_d:
                date = datetime.strptime(animal['created_on'], '%Y-%m-%d')
                if ((date<start) or (date>end)):
                        list2.append(animal)
        return jsonify({'animals without those in range': list2})

#returns the average number of legs per animal
@app.route('/animals/avgleg', methods = ['GET'])
def average_legs():
        test = get_data()
	animals_a = data['animals']
	leg_count = 0;
	for animal in animals_a:
		leg_count = leg_count + animal['legs']
	leg_avg = leg_count/len(animials_a)
	if(leg_avg > 0) :
		return jsonify({'average':leg_avg})
	else:
		return jsonify({'average': 0})
        

#returns a total count of animals
@app.route('/animals/total', methods = ['GET'])
def count_animals():
        test = get_data()
	animals_c = data['animals']
	total = len('animals')
        return jsonify ({'total':total})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

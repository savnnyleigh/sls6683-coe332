import unittest
from read_animals2 import breed

class TestParser(unittest.TestCase):

	def test_breed(self):
		parent1 = {'head': 'lion', 'body': 'gorilla-gelding', 'arms': 2, 'legs': 3, 'tail': 5}
		parent2 = {'head': 'lion', 'body': 'gorilla-gelding', 'arms': 2, 'legs': 3, 'tail': 5} 		
		self.assertEqual(breed(parent1, parent2)['head'], 'lion')
		self.assertEqual(breed(parent1, parent2)['body'], 'gorilla-gelding')
		self.assertEqual(breed(parent1, parent2)['arms'], 2)
		self.assertEqual(breed(parent1, parent2)['legs'], 3)
		self.assertEqual(breed(parent1, parent2)['tail'], 5)
		self.assertDictEqual(parent1, breed(parent1,parent2))
		self.assertRaises(TypeError, breed, True)
		self.assertRaises(TypeError, breed, 1)
		self.assertRaises(TypeError, breed, ['animal1','animal2'])


if __name__ == '__main__':
    unittest.main()

import random
import sys
import copy

"""

0 : 000
1 : 001
2 : 010
3 : 011
4 : 100
5 : 101
6 : 110
7 : 111

"""

class Rule(object):

	def __init__(self, rule_num):
		self._rule_num = rule_num
		self._rule_array = []
		for count in range(8):
			self._rule_array.append(0)
			self._rule_array[count] = ((rule_num)/(2**count))%2

	def getStateFromTriplet(self, left, center, right):
		if (left == 0) and (center == 0) and (right == 0):
			return self._rule_array[0]
		if (left == 0) and (center == 0) and (right == 1):
			return self._rule_array[1]
		if (left == 0) and (center == 1) and (right == 0):
			return self._rule_array[2]
		if (left == 0) and (center == 1) and (right == 1):
			return self._rule_array[3]
		if (left == 1) and (center == 0) and (right == 0):
			return self._rule_array[4]
		if (left == 1) and (center == 0) and (right == 1):
			return self._rule_array[5]
		if (left == 1) and (center == 1) and (right == 0):
			return self._rule_array[6]
		if (left == 1) and (center == 1) and (right == 1):
			return self._rule_array[7]

class Cell(object):

	def __init__(self, rule, state=0):
		self.setState(state)
		self._rule = rule

	def setState(self, state):
		self._state = state

	# todo: remove?
	def setStateFromProb(self, prob):
		random_num = random.random()
		if random_num < prob:
			self._state = 1
		else:
			self._state = 0

	def setStateFromLCR(self, left, center, right):
		# print(left, center, right)
		self._state = self._rule.getStateFromTriplet(left, center, right)

class Automaton(object):

	def __init__(self, length, rule):
		self._rule = Rule(rule)
		self._length = length
		self._cell_list = [Cell(self._rule, 0) for count in range(length)]

	def init_middle(self):
		if (self._length % 2) == 0:
			middle = self._length/2
		else:
			middle = (self._length + 1)/2
		self._cell_list[middle]._state = 1

	def evolve(self):
		# copy over the list
		new_cell_list = copy.deepcopy(self._cell_list)
		for index, cell in enumerate(new_cell_list):
			if index == self._length - 1:
				mod_index = 0
			else:
				mod_index = index
			# print cell._state
			cell.setStateFromLCR(self._cell_list[mod_index-1]._state, self._cell_list[mod_index]._state, self._cell_list[mod_index+1]._state)
			# print cell._state
		self._cell_list = copy.deepcopy(new_cell_list)

	def print_automaton(self):
		for cell in self._cell_list:
			if cell._state == 0:
				sys.stdout.write(' ')
			else:
				sys.stdout.write('-')
			sys.stdout.flush()
		sys.stdout.write('\n')
		sys.stdout.flush()


if __name__ == "__main__":
	# Demo Code #

	# create a new automaton of length 101 cells, that evolves with rule 129
	my_automaton = Automaton(101, 30)
	# initialize the middle cell as a seed
	my_automaton.init_middle()
	# print everything out
	my_automaton.print_automaton()
	# evolve and print 40 times
	for i in range(40):
		my_automaton.evolve()
		my_automaton.print_automaton()





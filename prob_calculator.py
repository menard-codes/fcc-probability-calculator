import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **kwargs):
		if len(kwargs) == 0:
			self.contents = ['black']
		else:
			self.contents = [color for color, amount in kwargs.items() for x in range(amount)]
			self.original_balls = copy.deepcopy(self.contents)

	def draw(self, num_of_draws):
		if num_of_draws > len(self.contents):
			return self.contents
		else:
			draws = []
			self.contents = copy.deepcopy(self.original_balls)
			for x in range(num_of_draws):
				choice = random.choice(self.contents)
				draws.append(choice)
				self.contents.remove(choice)
			return draws



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	if isinstance(hat, Hat):
		count = 0
		for _ in range(num_experiments):
			current_draw = hat.draw(num_balls_drawn)
			occured = 0
			for color, expected_occurences in expected_balls.items():
				if current_draw.count(color) >= expected_occurences:
					occured += 1
			if occured == len(expected_balls):
				count += 1
		return count / num_experiments
	else:
		return f'{hat} is invalid'

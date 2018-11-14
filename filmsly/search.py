###
### Author: Sam McCaffrey
###
###
###

import os

from difflib import SequenceMatcher


class search:

	def __init__(self, param):
		self.param = param.lower().strip()
		return

	def resolve_theatre_paramter(self, threshold = 0.9):
		_dir = os.path.join(os.path.dirname(__file__), 'theatres')
		theatres =  [f.split('.')[0] for f in os.listdir(_dir) if f.endswith('.py') and not f.startswith('__init__')]
		for theatre in theatres:
			compare = SequenceMatcher(None, self.param.lower().strip(), theatre).ratio()
			#print(compare)
			if compare >= threshold:
				return theatre
		print('The theatre {} could not be found.'.format(search_param))




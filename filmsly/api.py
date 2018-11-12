##
## Author: Sam McCaffrey
##
##

import os
import sys

#from filmsly.theatres.amc import amc_api
#from filmsly.theatres.harkins import harkins_api

#import filmsly

from filmsly import theatres

from .search import search

class filmsly_api:

	def __init__(self):
		return

	def list_of_theatres(self):
		_dir = os.path.join(os.path.dirname(__file__), 'theatres')
		return [f.split('.')[0] for f in os.listdir(_dir) if f.endswith('.py') and not f.startswith('__init__')]

	def get_theatre_info(self, theatre = 'ALL'):
		if theatre != 'ALL':
			resolve = search(param = theatre).resolve_theatre_paramter()
			class_name = resolve + '_api'
			_temp = getattr(theatres, class_name)
			_theatre_obj = _temp(chain = resolve)
			return _theatre_obj.get_theatre_info()
		print('Gathering all information for {} \nThis could take awhile.'.format(self.list_of_theatres()))

	def get_showtime(self):
		return

	def index_all_theatres(self):
		return

	def get_showtime(self, movie):
		""" Requires theatre_chain_index to exist
		"""
		return



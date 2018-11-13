##
## Author: Sam McCaffrey
##
##
##
##
##

import os
import sys

from datetime import datetime

from filmsly import theatres

from .search import search
from .databases import sqllite

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


	def _parse_parser_outputs(self, data: dict) -> tuple:
		"""Flattens parser outputs into a single list of tuples
		"""
		results = []
		chain_name = data['theatre_chain']
		chain_url = data['theatre_chain_url']
		#(theatre_chain_name,theatre_chain_url,theatre_location_name, \
		#theatre_location_url,movie_name,movie_showtimes_url_location,record_date)
		for theatre in data['theatres'].keys():
			for movie in data['theatres'][theatre]['theatre_showtimes'].keys():
				theatre_location_name = theatre
				theatre_location_url = data['theatres'][theatre]['theatre_location_url']
				movie_name = movie
				movie_showtimes_url_location = data['theatres'][theatre]['showtimes_url_location']
				now = datetime.now()
				record_date = now.strftime('%Y-%m-%dT%H')

				row = (chain_name,chain_url,theatre_location_name,theatre_location_url,movie_name,movie_showtimes_url_location,record_date)
				results.append(row)
		return results

	def index_theatre(self, theatre_name):
		resolve = search(param = theatre_name).resolve_theatre_paramter()
		_obj = filmsly_api()
		theatre_data = _obj.get_theatre_info(theatre = resolve)
		tupled_data = self._parse_parser_outputs(data = theatre_data)

		init_db = sqllite()

		for x in tupled_data:
			init_db.insert_index_record(data = x)

		init_db.close_and_commit()
		return


	def get_showtime(self, movie):
		""" Requires theatre_chain_index to exist
		"""
		return



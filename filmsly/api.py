##
## Author: Sam McCaffrey
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

	def get_showtime(self, movie, theatre=None):
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

	def _parse_parser_outputs(self, data: dict) -> tuple:
		"""Flattens parser outputs into a single list of tuples
		(theatre_chain_name,theatre_chain_url,theatre_location_name, \
		theatre_location_url,movie_name,movie_showtimes_url_location,record_date)
		"""
		results = []
		chain_name = data['theatre_chain']
		chain_url = data['theatre_chain_url']

		for theatre in data['theatres'].keys():
			for movie in data['theatres'][theatre]['theatre_showtimes'].keys():
				theatre_location_name = theatre
				theatre_location_url = data['theatres'][theatre]['theatre_location_url']
				movie_name = movie
				movie_showtimes_url_location = data['theatres'][theatre]['showtimes_location_url']
				now = datetime.now()
				record_date = now.strftime('%Y-%m-%d:%H')
				row = (chain_name,chain_url,theatre_location_name,theatre_location_url,movie_name,movie_showtimes_url_location,record_date)
				results.append(row)
		return results

	def index_all_theatres(self):
		print('\n Rebuilding Entire Index!\n\n Grab some coffee!')
		### Iterate through all theatre names
		### Call each crawler
		### Pass each results to results parser
		### write each result to database
		for theatre_chain in self.list_of_theatres():
			_temp_obj = filmsly_api()
			theatre_data = _temp_obj.get_theatre_info(theatre = theatre_chain)
			tupled_data = self._parse_parser_outputs(data = theatre_data)
			init_db = sqllite()
			### Delete old data corsponding to theatre name
			init_db.delete_theatre_records(theatre_name = theatre_chain)
			for x in tupled_data:
				init_db.insert_index_record(data = x)
			init_db.close_and_commit()
		return

	def index_theatre(self, theatre_name):
		resolve = search(param = theatre_name).resolve_theatre_paramter()
		_obj = filmsly_api()
		theatre_data = _obj.get_theatre_info(theatre = resolve)
		tupled_data = self._parse_parser_outputs(data = theatre_data)
		init_db = sqllite()

		### Delete old data corsponding to theatre name
		init_db.delete_theatre_records(theatre_name = resolve)
		for x in tupled_data:
			init_db.insert_index_record(data = x)
		init_db.close_and_commit()
		return




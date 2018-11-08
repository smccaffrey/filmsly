import os

from filmsly.theatres.amc import amc_api
from filmsly.theatres.harkins import harkins_api

class filmsly_api:

	def __init__(self):
		return

	def get_theatres(self, theatre = 'ALL'):
		print('Get theatres class successfully called.')
		harkins_api().get_theatre_info("https://www.harkins.com/locations")
		#amc_api().gather_city_info("https://www.amctheatres.com/movie-theatres")
		return harkins_api().get_theatre_info("https://www.harkins.com/locations")

	def list_of_theatres(self):
		_dir = os.path.join(os.path.dirname(__file__), 'theatres')
		return [f.split('.')[0] for f in os.listdir(_dir) if f.endswith('.py') and not f.startswith('__init__')]



#from __future__ import absolute_import

#from . import harkins_api
from filmsly.theatres.amc.parser import amc_api

class filmsly_api:

	def __init__ (self):
		return

	def get_theatres(self, theatre = 'ALL'):
		print('Get theatres class successfully called.')
		return amc_api().gather_city_info("https://www.amctheatres.com/movie-theatres")


	def list_of_theatres(self):
		return


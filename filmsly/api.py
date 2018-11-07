
from filmsly.theatres.amc.parser import amc_api
from filmsly.theatres.harkins.parser import harkins_api

class filmsly_api:

	def __init__(self):
		return

	#print('filmsly api doorway created')
	#def __init__ (self, theatre = 'test'):
	#	self.t = theatre

	def test(self):
		return 'Test successful'

	def get_theatres(self, theatre = 'ALL'):
		print('Get theatres class successfully called.')
		harkins_api().get_theatre_info("https://www.harkins.com/locations")
		amc_api().gather_city_info("https://www.amctheatres.com/movie-theatres")
		return


	def list_of_theatres(self):
		return 


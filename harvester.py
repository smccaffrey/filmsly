import requests

from bs4 import BeautifulSoup

from filmsly.theatres.harkins.parser import harkins_api
from filmsly.theatres.amc.parser import amc_api
#from filmsly.theatres.progress import progressBar

from filmsly.api import filmsly_api

if __name__ == '__main__':

	_test = filmsly_api()
	_test.get_theatres()

	### Harkins
	#current_harkins_data = harkins_api().get_theatre_info("https://www.harkins.com/locations")
	
	### AMC
	current_amc_data = amc_api().gather_city_info("https://www.amctheatres.com/movie-theatres")
	#test = amc_api()._gather_theatre_info("https://www.amctheatres.com/movie-theatres/atlanta")
	#print(test)
	#amc_api()._gather_showtime_info("https://www.amctheatres.com/movie-theatres/atlanta/amc-camp-creek-14/showtimes/all/2018-10-28/amc-camp-creek-14/all")
	#amc_api()._gather_showtime_info("https://www.amctheatres.com/movie-theatres/atlanta/amc-camp-creek-14/showtimes")


	 
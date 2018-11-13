import requests

from bs4 import BeautifulSoup
from datetime import datetime

from ..library.progress import progressBar

class amc_api:

	def __init__ (self, chain):
		self._progress = progressBar()
		self.root_url = "https://www.amctheatres.com"
		self.root_url_locations = "https://www.amctheatres.com/movie-theatres"
		self.timestamp = datetime.today().strftime('%Y-%m-%d')
		self.results = {}
		self.results['theatre_chain'] = chain
		self.results['theatre_chain_url'] = self.root_url_locations
		#self.results['theatres'] = {}
		return

	def _gather_showtime_info(self, theatre_url: str) -> dict:
		re = requests.get(theatre_url)
		soup = BeautifulSoup(re.text, 'html.parser')
		#movies = soup.find('div', {'class' : 'ShowtimesByTheatre-maincol-scroll'}) #not robust
		movies = soup.find_all('div', {'class' : 'ShowtimesByTheatre-film'}) #more robust
		results = {}
		for movie in movies:
			title = movie.find('a', {'class' : 'MovieTitleHeader-title'}).text
			active_showtimes = movie.find_all('div', {'class' : 'Showtime'})
			inactive_showtimes = movie.find_all('div', {'class' : 'Showtime Showtime-disabled'})
			inactive = [x.text for x in inactive_showtimes]
			active = [x.text for x in active_showtimes]
			#print(title, active)
			results[title] = {}
			results[title]['active_showtimes'] = active
			results[title]['inactive_showtimes'] = inactive
		return results

	def _gather_theatre_info(self, theatres_info_list: list) -> dict:
		i = 0
		results = {}
		for city,url in theatres_info_list:

			self._progress.otherProgressBar(i, total = len(theatres_info_list), label = 'AMC: ', end_label = city)
			i += 1

			re = requests.get(url)
			soup = BeautifulSoup(re.text, 'html.parser')
			theatres = soup.find('ul', {'class' : 'PanelList u-listUnstyled '})
			for theatre in theatres:
				name = theatre.find('span', {'class' : 'Link-text Headline--h3'}).text
				address = "".join(theatre.find('span', {'class' : 'Link-text txt--thin'}).text.splitlines()).replace("  ", "")
				showtime_link = theatre.find('a', {'class' : 'Link Link--arrow'})['href']
				#print(name + " | " + address)
				#print(self.root_url + showtime_link)
				results[name] = {}
				results[name]['address'] = address
				results[name]['city'] = city
				results[name]['state'] = ""
				results[name]['zip'] = ""
				results[name]['showtimes_url_location'] = self.root_url + showtime_link + '/showtimes/all/' + self.timestamp + '/' + showtime_link.split('/')[3] + '/all'
				results[name]['theatre_location_url'] = self.root_url + showtime_link + '/showtimes/all/' + self.timestamp + '/' + showtime_link.split('/')[3] + '/all'
				results[name]['theatre_showtimes'] = self._gather_showtime_info(results[name]['showtime_link'])
				#print(results[name]['showtime_link'])
				#"https://www.amctheatres.com/movie-theatres/atlanta/amc-camp-creek-14/showtimes/all/2018-10-28/amc-camp-creek-14/all"
		#print(results)
		return results

	def get_theatre_info(self) -> dict:
		re = requests.get(self.root_url_locations)
		soup = BeautifulSoup(re.text, 'html.parser')
		#results = {}
		#results['theatre_chain'] = self.chain
		cities_raw = soup.find('ul', {'class' : 'u-listUnstyled LinkList'})
		cities = [[x.text, self.root_url + x.find('a')['href']] for x in cities_raw]
		#i = 0
		#for k,v in cities:
		#self._progress.otherProgressBar(i, total = len(cities), label = 'AMC: ', end_label = k)
		self.results['theatres'] = self._gather_theatre_info(theatres_info_list = cities)
		#	i += 1
		return self.results

if __name__ == '__main__':
	print('Running Tests ... ')
	temp = amc_api(chain = 'amc').gather_city_info("https://www.amctheatres.com/movie-theatres")

	#amc_api()._gather_theatre_info("https://www.amctheatres.com/movie-theatres/albany-ga")

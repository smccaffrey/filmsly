import requests

from bs4 import BeautifulSoup
from datetime import datetime

#from info import amc_crawling_info as ACI

from ...library.progress import progressBar

class amc_api:

	def __init__ (self):
		self._progress = progressBar()
		self.root_url = "https://www.amctheatres.com"
		self.timestamp = datetime.today().strftime('%Y-%m-%d')
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

	def _gather_theatre_info(self, url: str) -> dict:

		re = requests.get(url)
		soup = BeautifulSoup(re.text, 'html.parser')
		theatres = soup.find('ul', {'class' : 'PanelList u-listUnstyled '})
		results = {}
		for theatre in theatres:
			name = theatre.find('span', {'class' : 'Link-text Headline--h3'}).text
			address = "".join(theatre.find('span', {'class' : 'Link-text txt--thin'}).text.splitlines()).replace("  ", "")
			showtime_link = theatre.find('a', {'class' : 'Link Link--arrow'})['href']
			#print(name + " | " + address)
			#print(self.root_url + showtime_link)
			results[name] = {}
			results[name]['address'] = address
			results[name]['showtime_link'] = self.root_url + showtime_link + '/showtimes/all/' + self.timestamp + '/' + showtime_link.split('/')[3] + '/all'
			results[name]['showtimes'] = self._gather_showtime_info(results[name]['showtime_link'])
			#print(results[name]['showtime_link'])
			#"https://www.amctheatres.com/movie-theatres/atlanta/amc-camp-creek-14/showtimes/all/2018-10-28/amc-camp-creek-14/all"
		return results

	def gather_city_info(self, url: str) -> dict:
		re = requests.get(url)
		soup = BeautifulSoup(re.text, 'html.parser')
		results = {}
		cities_raw = soup.find('ul', {'class' : 'u-listUnstyled LinkList'})
		cities = [[x.text, self.root_url + x.find('a')['href']] for x in cities_raw]
		results = {}
		i = 0
		for k,v in cities:
			self._progress.otherProgressBar(i, total = len(cities), label = 'AMC: ', end_label = k)
			results['city'] = k
			results['theatres'] = self._gather_theatre_info(v)
			#print(k + "|" + v)
			i += 1
		return results

if __name__ == '__main__':
	print('Running Tests ... ')
	#temp = amc_api().gather_city_info("https://www.amctheatres.com/movie-theatres")

	amc_api()._gather_theatre_info("https://www.amctheatres.com/movie-theatres/albany-ga")

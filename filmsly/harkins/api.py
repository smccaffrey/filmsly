import requests

from bs4 import BeautifulSoup

from .config.info import harkins_crawling_info as HCI
from ..progress import progressBar

class harkins_api:

	def __init__(self):
		"""Harkins Theatre Information API
		"""
		self._progress = progressBar()
		return

	def _get_showtimes(self, url: str) -> dict:
		re = requests.get(url)
		soup = BeautifulSoup(re.text, 'html.parser')
		movies = soup.find_all('li', {'class' : 'ease-in-up'})
		results = {}
		for movie_index in range(len(movies)):
			info = movies[movie_index].find('h4')
			name = info.find('a').text.strip()
			times = [x for x in movies[movie_index].find('ul', {'class' : 'showtimes'}).text.strip().split('\n\n\n')]
			results[name] = times
			#print(name, times)
		return results

	def get_theatre_info(self, url: str) -> dict:
		"""Gather's all theatre information for the targeted theatre
		"""
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		regions = soup.find_all(HCI.REGIONS_TAG, {'class' : HCI.REGIONS_CLASS})
		region_cnt = len(regions)
		results = {}
		index = 0
		for region_index in range(region_cnt):
			region_nm = regions[region_index].find(HCI.REGION_TAG, {'class' : HCI.REGION_CLASS}).text
			theatres = regions[region_index].find_all(HCI.THEATRES_TAG, {'class' : HCI.THEATRES_CLASS})
			theatre_cnt = len(theatres)
			#self._progress.printProgressBar(0, theatre_cnt, suffix = 'Complete', length = 50)
			#self._progress.otherProgressBar(region_index, total = region_cnt, label = 'Harkins')

			for theatre_index in range(theatre_cnt):
				#print('Gathering Data for Theatre {}/{}'.format(theatre_index, len(theatres)))
				#self._progress.printProgressBar(theatre_index, theatre_cnt, prefix = 'Harkins', suffix = 'Complete', length = 50)
				self._progress.otherProgressBar(theatre_index, total = theatre_cnt, label = 'Harkins - {}'.format(region_nm))
				info = theatres[theatre_index].find(HCI.THEATRE_TAG, {'class' : HCI.THEATRE_CLASS})
				name = info.text.strip()
				showtimes_link = HCI.ROOT_URL + info.find('a')['href']
				address = theatres[theatre_index].find('div', {'class' : 'address'}).text.strip()
				phone = theatres[theatre_index].find('div', {'class' : 'phone'}).text.strip()
				results[name] = {}
				results[name]['index'] = index
				results[name]['region'] = region_nm
				results[name]['address'] = address
				results[name]['phone'] = phone
				results[name]['showtimes_link'] = showtimes_link
				results[name]['showtimes'] = self._get_showtimes(showtimes_link)
				index += 1
				
		return results

if __name__ =='__main__':
	print('Running Tests on {}'.format(__name__))

	TEST_THEATRE = "https://www.harkins.com/locations"
	TEST_ROOT = "https://www.harkins.com"
	TEST_TIMES = "https://www.harkins.com/locations/moreno-valley-16"

	print('Testing get_theatre_info')
	if harkins_api().get_theatre_info(TEST_THEATRE):
		print('Test Passed!')
	else:
		print('Test Failed!')

	print('Testing _get_showtimes')
	if harkins_api()._get_showtimes(TEST_TIMES):
		print('Test Passed!')
	else:
		print('Test Failed')
import requests

from bs4 import BeautifulSoup

from ..library.progress import progressBar

class harkins_api:

	def __init__(self, chain):
		"""Harkins Theatre Information API
		"""
		self.root_url = "https://www.harkins.com/locations"
		self._progress = progressBar()
		self.results = {}
		self.results['theatre_chain'] = chain
		self.results['theatre_chain_url'] = self.root_url
		self.results['theatres'] = {}
		return

	def theatre_info(self):

		return self.results

	def get_showtimes(self, url: str) -> dict:
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

	def get_theatre_info(self) -> dict:
		"""Gather's all theatre information for the targeted theatre
		"""
		r = requests.get(self.root_url)
		soup = BeautifulSoup(r.text, 'html.parser')
		regions = soup.find_all('div', {'class' : 'region'})
		region_cnt = len(regions)
		results = {}
		index = 0
		for region_index in range(region_cnt):
			region_nm = regions[region_index].find('h3', {'class' : 'underlined'}).text
			theatres = regions[region_index].find_all('div', {'class' : 'details col-5/8 shift5-full'})
			theatre_cnt = len(theatres)
			for theatre_index in range(theatre_cnt):
				self._progress.otherProgressBar(theatre_index, total = theatre_cnt, label = 'Harkins - {}'.format(region_nm))
				info = theatres[theatre_index].find('h4', {'class' : 'underlined tooltip-trigger'})
				name = info.text.strip()
				showtimes_link = 'https://www.harkins.com' + info.find('a')['href']
				address = theatres[theatre_index].find('div', {'class' : 'address'}).text.strip()
				phone = theatres[theatre_index].find('div', {'class' : 'phone'}).text.strip()
				self.results['theatres'][name] = {}
				self.results['theatres'][name]['address'] = address
				self.results['theatres'][name]['city'] = region_nm
				self.results['theatres'][name]['state'] = ""
				self.results['theatres'][name]['zip'] = ""
				self.results['theatres'][name]['phone'] = phone
				self.results['theatres'][name]['theatre_location_url'] = showtimes_link
				self.results['theatres'][name]['theatre_showtimes'] = self.get_showtimes(showtimes_link)
				self.results['theatres'][name]['showtimes_url_location'] = showtimes_link
				index += 1
				
		return self.results

if __name__ =='__main__':
	print('Running Tests on {}'.format(__name__))

	TEST_THEATRE = "https://www.harkins.com/locations"
	TEST_ROOT = "https://www.harkins.com"
	TEST_TIMES = "https://www.harkins.com/locations/moreno-valley-16"

	print('Testing get_theatre_info')
	if harkins_api(chain = 'harkins').get_theatre_info(TEST_THEATRE):
		print('Test Passed!')
	else:
		print('Test Failed!')

	print('Testing get_showtimes')
	if harkins_api(chain = 'harkins').get_showtimes(TEST_TIMES):
		print('Test Passed!')
	else:
		print('Test Failed')
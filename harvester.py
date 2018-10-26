import requests

from bs4 import BeautifulSoup

from harvester.harkins.api import harkins_api

if __name__ == '__main__':

	current_harkins_data = harkins_api().get_theatre_info("https://www.harkins.com/locations")
	print(current_harkins_data.keys())

	 
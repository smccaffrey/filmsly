import scrapy
import requests


class Showtimes(scrapy.Spider):
	name = "showtimes"

	def __init__(self):
		self.root_url = 'https://www.harkins.com'

	def start_requests(self):
		urls = ['https://www.harkins.com/locations']
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		page = response.url
		t_xpath = "//*[@id="+"\""+"site-wrapper"+"\""+"]/main/section/div/div[2]/div[1]/ul/li"
		for region in response.css("div.region"):
			for theatre in region.xpath(t_xpath):
				sub_url = theatre.css("h4.underlined.tooltip-trigger a::attr(href)").extract_first()
				next_url = self.root_url + sub_url
				#showtimes = scrapy.Request(url = next_url)
				showtimes = self.parse_theatre(scrapy.http.Response(url=next_url))
				#print(next_url)
				yield {
					'root_url' : page,
					'region' : region.css("h3::text").extract()[0],
					'theatre' : theatre.css("h4.underlined.tooltip-trigger a::text").extract_first().strip(),
					'address' : self.parse_addr(theatre.css("div.address::text").extract()),
					'phone' : theatre.css("div.phone a::text").extract_first(),
					'theatre_url' : next_url,
					'showtimes' : showtimes
				}	

	def parse_theatre(self, response):
		page = response.url
		res = {}
		#print(response)
		for showtime in response.css("div.cols"):
			#res['url'] = page
			res['movie'] = showtime.css("h4 a::text").extract_first().strip()
			res['movie_url'] = showtime.css("h4 a::attr(href)").extract_first()
		return res


	def parse_addr(self, address):
		return ' '.join(address).strip()
import scrapy
import datetime

class AMC(scrapy.Spider):
	name = "amc"

	def __init__(self):
		self.root_url = "https://www.amctheatres.com"

	def start_requests(self):
		urls = ['http://www.amctheatres.com/movie-theatres']
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		temp = 'a.Link.Link--arrow.Link--reversed.Link--arrow--txt--tiny.txt--tiny'
		for market in response.css(temp):
			results = {
				'root_url' : self.root_url,
				'market' : market.css('::text').extract_first(),
				'market_url' : market.css('::attr(href)').extract_first()
			}
			market_url = self.root_url + results['market_url']
			request = scrapy.Request(url = market_url, callback = self.parse_market)
			request.meta['market_info'] = results
			yield request
		#class="Link Link--arrow Link--reversed Link--arrow--txt--tiny txt--tiny"

	def parse_market(self, response):
		results = response.meta['market_info']
		results['theatre'] = {}
		for theatre in response.css('li.PanelList-li'):
			name = theatre.css('div h3 a span::text').extract_first()
			today = datetime.datetime.today().strftime('%Y-%m-%d')
			showtimes_sub_url = theatre.css('div.TheatreFinder-links a::attr(href)').extract_first()
			showtimes_url = self.root_url + showtimes_sub_url + '/all/'+ today + '/' + showtimes_sub_url.split('/')[-2] + '/all'
			results['theatre']['name'] = name
			results['theatre']['address'] = theatre.css('div.TheatreInfo p a span::text').extract_first()
			results['theatre']['showtimes_url'] = showtimes_sub_url
			request = scrapy.Request(url = showtimes_url, callback = self.parse_theatre)
			request.meta['market_and_theatre_info'] = results
			yield request


	def parse_theatre(self, response):
		results = response.meta['market_and_theatre_info']
		results['theatre']['showtimes'] = {}
		for movie in response.css('div.ShowtimesByTheatre-film'):
			title = movie.css('a.MovieTitleHeader-title h2::text').extract()[0]
			results['theatre']['showtimes'][title] = {}
			#results['theatre']['showtimes']['title_info_url'] = movie.css('a.MovieTitleHeader-title::attr(href)').extract()
			#results['theatre']['showtimes'][title]['times'] = {}
			for showtime in movie.css('section.ShowtimeButtons'):
				results['theatre']['showtimes'][title]['times'] = showtime.css('a::text').extract()
				#time = showtime.css('a::text').extract()
				#results['theatre']['showtimes'][title]['times'][time] = showtime.css('a::attr(href)').extract()
		yield results




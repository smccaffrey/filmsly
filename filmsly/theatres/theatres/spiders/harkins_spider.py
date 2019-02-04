
import scrapy 

class Harkins(scrapy.Spider):
	name = "harkins"

	def __init__(self):
		self.root_url = 'https://www.harkins.com'

	def start_requests(self):
		urls = ['https://www.harkins.com/locations']
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	# def parse(self, response):
	# 	page = response.url
	# 	t_xpath = "//*[@id="+"\""+"site-wrapper"+"\""+"]/main/section/div/div[2]/div[1]/ul/li"
	# 	for region in response.css("div.region"):
	# 		for theatre in region.xpath(t_xpath):
	# 			sub_url = theatre.css("h4.underlined.tooltip-trigger a::attr(href)").extract_first()
	# 			next_url = self.root_url + sub_url
	# 			#showtimes = self.parse_theatre(requests.get(url = next_url))
	# 			#showtimes = scrapy.Request(url = next_url, callback = self.parse_theatre)
	# 			#showtimes = self.parse_theatre(scrapy.http.TextResponse(body = response.body,url=next_url))
	# 			#print(next_url)
	# 			results =  {
	# 				'root_url' : page,
	# 				'region' : region.css("h3::text").extract()[0],
	# 				'theatre' : theatre.css("h4.underlined.tooltip-trigger a::text").extract_first().strip(),
	# 				'address' : self.parse_addr(theatre.css("div.address::text").extract()),
	# 				'phone' : theatre.css("div.phone a::text").extract_first(),
	# 				'theatre_url' : next_url
	# 				#'showtimes' : showtimes
	# 			}
	# 			request = scrapy.Request(url = next_url, callback = self.parse_theatre) 
	# 			request.meta['theatre_info'] = results
	# 			yield request

	def parse(self, response):
		t_xpath = "div.theatre.cols"
		for theatre in response.css(t_xpath):
			sub_url = theatre.css("h4.underlined.tooltip-trigger a::attr(href)").extract_first()
			next_url = self.root_url + sub_url
			results =  {
				'root_url' : self.root_url,
				'theatre' : theatre.css("h4.underlined.tooltip-trigger a::text").extract_first().strip(),
				'address' : self.parse_addr(theatre.css("div.address::text").extract()),
				'phone' : theatre.css("div.phone a::text").extract_first(),
				'theatre_url' : sub_url
			}
			request = scrapy.Request(url = next_url, callback = self.parse_theatre) 
			request.meta['theatre_info'] = results
			yield request

	def parse_theatre(self, response):
		results = response.meta['theatre_info']
		results['movies'] = {}
		for showtime in response.css("div.cols"):
			title = showtime.css("h4 a::text").extract_first()
			m_url = showtime.css("h4 a::attr(href)").extract_first()
			results['movies'][str(title).strip()] = m_url
			
		yield results

	def parse_addr(self, address):
		return ' '.join(address).strip()

 		
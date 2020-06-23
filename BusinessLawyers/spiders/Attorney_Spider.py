import scrapy

class LawyerSpider(scrapy.Spider):
	name = 'lawyers'

	base_url = 'https://www.justia.com/lawyers/business-law/texas/houston'

	def start_requests(self):

		yield scrapy.Request(
			url = self.base_url,
			callback = self.parse)


	def parse(self, response):
		for lawyer_card in response.css('div[class="lawyer-card-aligner"]'):
			print(lawyer_card.css('strong[class="-phone"] a::text').get())
			print(lawyer_card.css('a[class="url main-profile-link"] span::text').get())




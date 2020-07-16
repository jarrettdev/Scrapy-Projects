import scrapy
import json
import csv

class LawyerSpider(scrapy.Spider):
	name = 'lawyers'

	custom_setting = {
		'FEED_FORMAT':'csv',
		'FEED_URI':'lawyers.csv'
	}

	base_url = 'https://www.justia.com/lawyers/business-law/texas/houston'

	def start_requests(self):

		for page in range(0,25):
			next_page = self.base_url + '?page=' + str(page)
			yield scrapy.Request(url = next_page, callback = self.parse)


	def parse(self, response):

		for lawyer_card in response.css('div[class="lawyer-card-aligner"]'):
			items = {
			'number': lawyer_card.css('strong[class="-phone"] a::text').get(),
			'name': lawyer_card.css('a[class="url main-profile-link"] span::text').get()
			}

			yield items




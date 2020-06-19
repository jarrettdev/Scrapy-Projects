#Scrape best sellings guns + prices from Buds Gun Shop.
#Jarrett Dev

import scrapy

class GunSpider(scrapy.Spider):
    name = "gun_scraper"

    #output
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'gun_prices.csv'
    }

    def start_requests(self):
    	#base url
        url = 'https://www.budsgunshop.com/search.php/type/Firearms/sort/best-selling/'

        #pagination
        for page in range(1, 24):
            next_page = url + 'page/' + str(page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse(self, response):
        for card in response.css('div[class="row"] div[class="col-lg-4 col-md-4 col-sm-4 col-xs-4 list-products"]'):
            items = {
                'product': card.css('a[class="product-box-link"] div p span[itemprop="name"]::text').get(),
                'price': ''.join(card.css('div[class="list-products-info-container"] div div font *::text').getall())
            }
            yield items

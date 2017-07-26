# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from string import whitespace
import requests

class VirginStoresSpider(scrapy.Spider):
    name = "virgin_stores"
    allowed_domains = ["stores.virginmobileusa.com"]

    @staticmethod
    def generate_base_urls():
        """Generate url to star scrapping based on the zip codes
            by example: http://stores.virginmobileusa.com/cgi-bin/search.pl?zipcode=92656&phones=Yes&topup=No&b2g=No&iph=No&page=2
        """
        with open('', 'r') as zipcodes_file:
            for line in zipcodes_file:
                line = line.split(',')
                try:
                    zipcode = int(line[0])
                    yield 'http://stores.virginmobileusa.com/cgi-bin/search.pl?zipcode={zipcode}&phones=Yes&topup=No&b2g=No&iph=No&page=1'\
                        .format(zipcode=line[0])
                except:
                    pass

    start_urls = generate_base_urls.__func__()

    def parse(self, response):
        search_quota_limit_reached = response.xpath('//p/text()').extract_first()
        if 'You have reached the maximum search quota.' in search_quota_limit_reached:
            self.logger.warning("Quota limit reached, adding to the retry list %s", response.url)
            yield Request(response.url, callback=self.parse, dont_filter=True)
        else:
            for store_entry in response.xpath('//tbody/tr'):
                city_state_zipcode = store_entry.xpath('./td[@class="address"]/text()[2]')\
                    .extract_first(default='not found').strip(whitespace).splitlines()

                while len(city_state_zipcode) < 3:
                    city_state_zipcode.append('not found')

                products = store_entry.xpath('./td[@class="direction"]/text()').extract_first(default='not found')
                item = {
                    'store_name': store_entry.xpath('./td[@class="store_name"]/text()').extract_first(default='not found'),
                    'address': store_entry.xpath('./td[@class="address"]/text()').extract_first(default='not found'),
                    'phone': store_entry.xpath('./td[@class="phone"]/text()').extract_first(default='not found'),
                    'city': city_state_zipcode[0].strip(whitespace),
                    'state': city_state_zipcode[1].strip(whitespace),
                    'zipcode': city_state_zipcode[2].strip(whitespace),
                    'product_phone': 'Phones' in products,
                    'product_topup_card': 'Top-Up Cards' in products,
                    'product_broadband2go': 'Broadband2Go' in products
                }

                if item['store_name'] != 'not found':
                    yield item

            next_page = response.xpath('//td[@class="pagination"]/a[. = ">"]/@href').extract_first()
            if next_page is not None:
                yield Request(next_page, callback=self.parse)

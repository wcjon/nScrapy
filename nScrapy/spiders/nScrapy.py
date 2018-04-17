# -*- coding: utf-8 -*-
"""
Scrape Newegg URLs using a list of IDs
"""

import scrapy

class nScrapy(scrapy.Spider):
	name = 'nScrapy'
	allowed_domains = ['newegg.com']
	start_urls = ["https://www.newegg.com/Product/Product.aspx?Item=050-013N-00001"]
		
	def parse(self, response):
		livePage = response.xpath('//script[contains(text(), "pstatus")]/text()').extract_first()
		yield {
			'Page ID': response.css('input#persMainItemNumber').xpath('@value').extract_first(),
			'Page URL': response.url, 
			'Script Found on Page': response.css('div#wc-power-page').extract_first(),
			'Live Status': livePage[livePage.index("pstatus"):livePage.index("&ptype")][8:],
		}

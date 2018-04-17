# -*- coding: utf-8 -*-
"""
Scrape Newegg URLs using a list of IDs
"""

import scrapy
import time
#from time import sleep

class nScrapy(scrapy.Spider):
	name = 'nScrapy'
	allowed_domains = ['newegg.com']
#	with open("ids.txt", "rt") as f:
#		start_urls = ["https://www.newegg.com/Product/Product.aspx?Item=" + url.strip() for url in f.readlines()]
	start_urls = ["https://www.newegg.com/Product/Product.aspx?Item=050-013N-00001"]
		
	def parse(self, response):
		time.sleep(10)
		livePage = response.xpath('//script[contains(text(), "pstatus")]/text()').extract_first()
		yield {
			'Page ID': response.css('input#persMainItemNumber').xpath('@value').extract_first(),
			'Page URL': response.url, 
			'Script Found on Page': response.css('div#wc-power-page').extract_first(),
			'Live Status': livePage[livePage.index("pstatus"):livePage.index("&ptype")][8:],
		}

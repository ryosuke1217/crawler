# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy_sch.items import ScrapySchItem


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['chiebukuro.yahoo.co.jp']
    start_urls = ['https://chiebukuro.yahoo.co.jp/']
    # DOMEIN = "https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/"

    def parse(self, response):
        domein = "https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/"
        for url in response.css("a::attr('href')").extract():
            if not url.startswith('https://'):
                continue
            if domein not in url:
                yield scrapy.Request(url, callback=self.parse)
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    
    def parse_dir_contents(self, response):
        items = ScrapySchItem()
        items["question"] = ''.join(response.css('div.sttsRslvd div.ptsQes p::text').extract())
        items["answer"] = ''.join(response.css('div.mdPstdBA div.ptsQes p::text').extract())
        items['url'] = response.url
        return items
    
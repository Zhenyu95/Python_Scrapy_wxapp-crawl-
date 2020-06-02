# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappunionSpider(CrawlSpider):
    name = 'wxappUnion'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'http.+mod=list&catid=1&page=\d'), follow=False),
        Rule(LinkExtractor(allow=r'http.*article-\d{4}-\d\.html'),callback='parse_detail',follow=False)
    )
    def parse_detail(self, response):
        item = {}
        item['title'] = response.xpath('//h1[@class="ph"]/text()').get()
        item['author'] = response.xpath('//p[@class="authors"]/a/text()').get()
        item['time'] = response.xpath('//span[@class="time"]/text()').get()
        item['content'] =''.join(response.xpath('//td[@id="article_content"]//text()').getall()).strip()
        yield item
        
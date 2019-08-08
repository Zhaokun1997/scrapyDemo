import scrapy

from tutorial.items import ZgdirItem


class ZgdirSpider(scrapy.Spider):
    name = "zgdir"
    allowed_domains = ['zgdir.org']
    start_urls = ['http://www.zgdir.org/']

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//tr/td')
        items = []
        for site in sites:
            item = ZgdirItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            items.append(item)

        return items


#--*coding:utf-8 --*
import scrapy
from scrapy.http.request import Request
from metro.items import MetroItem


class MetroSpider(scrapy.Spider):
    name = "metro"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Shanghai_Metro"
    ]
    def parse(self, response):
        urlList=list()
        sellList=response.xpath("//*[@id='mw-content-text']/div/table/tbody/tr/td/span/a")
        for sel in sellList:
            link=sel.xpath('@href').extract()  #  提取各个地铁轨交线链接
            for ele in link:
                if "line" in ele or "Line" in ele or "train" in ele:
                    newUrl="https://en.wikipedia.org"+ele
                    yield Request(newUrl, callback=self.parse1)
    def parse1(self, response):
        item=MetroItem()
        item["stationName"] = response.xpath("//*[@id='mw-content-text']/div/table/tbody/tr/td/span/span/text()").extract()
        item['fileName']=response.url.split("/")[-1].replace('()',"")
        yield  item
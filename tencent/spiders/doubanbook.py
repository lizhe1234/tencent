# -*- coding: utf-8 -*-

import scrapy
from tencent.items import DoubanbookItem

class DoubanbookSpider(scrapy.Spider):
    """
    豆瓣读书Top250爬虫
        学习使用Twisted异步框架的功能,实现异步保存数据到MySQL数据库中
    """
    name = 'doubanbook'
    allowed_domains=['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?keywords=&tid=0&start=0#a']
    # def start_requests(self):
    #     base_url='https://book.douban.com/top250?start='
    #     offset=0
    #     start_urls=[base_url+str((offset+x)*25) for x in range(10)]
    #     for start_url in start_urls:
    #         yield scrapy.Request(url=start_url,callback=self.parse)

    def parse(self, response):
        list=response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        print(list)
        print('hahah')
        for infos in list:
            item=DoubanbookItem()
            item['positionname']=infos.xpath("./td[1]/a/text()").extract()[0]
            item['positionlink']=infos.xpath("./td[1]/a/@href").extract()[0]
            item['positionType']=infos.xpath("./td[2]/text()").extract()[0]
            item['positionNum']=infos.xpath("./td[3]/text()").extract()[0]
            item['positionLocation']=infos.xpath("./td[4]/text()").extract()[0]
            item['publishTime']=infos.xpath("./td[5]/text()").extract()[0]

            yield item
        next_link = response.xpath("//a[@id='next']/@href").extract()

        if next_link:
            next_link = next_link[0]
            print(next_link)
            yield scrapy.Request("https://hr.tencent.com/" + next_link, callback=self.parse)

        # tr_nodes=response.xpath('//div[@class="indent"]//tr')
        #
        # for tr_node in tr_nodes:
        #     link=tr_node.xpath('.//div[@class="pl2"]/a/@href').extract_first()
        #     title=tr_node.xpath('.//div[@class="pl2"]/a/text()').re(r'\w+')[0]
        #     info=tr_node.xpath('.//p[@class="pl"]/text()').extract_first()
        #     rating=tr_node.xpath('.//span[@class="rating_nums"]/text()').extract_first()
        #     quote=tr_node.xpath('.//span[@class="inq"]/text()').extract_first()
        #
        #     item=DoubanbookItem()
        #     item['link']=link
        #     item['title']=title
        #     item['info']=info
        #     item['rating']=rating
        #     item['quote']=quote
        #     yield item
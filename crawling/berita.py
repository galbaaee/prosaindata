from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.antaranews.com/terkini',
            'https://www.antaranews.com/terkini/2',
            'https://www.antaranews.com/terkini/3',
            'https://www.antaranews.com/terkini/4',
            'https://www.antaranews.com/terkini/5',
            'https://www.antaranews.com/terkini/6',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range (1,15):
        
            for news in response.css('#main-container > div.main-content.mag-content.clearfix > div'):
                yield{
                    'Judul Berita':news.css('div.col-md-8 > article:nth-child('+ str(i) +') > header > h3 > a::text').extract(),
                    'Jenis Berita':news.css('div.col-md-8 > article:nth-child('+ str(i) +') > header > p > a::text').extract(),
                    'Tanggal Rilis':news.css('div.col-md-8 > article:nth-child(8) > header > p > span::text').extract(),
                }
                
                

#load-content > div:nth-child(1) > div.article-list-info.content_center > span > a.article-list-title > h2
#load-content > div:nth-child(6) > div.article-list-info.content_center > span > a.article-list-title
#load-content > div:nth-child(6) > div.article-list-info.content_center > span > a.article-list-title > h2
#load-content > div:nth-child(7) > div.article-list-info.content_center > span > a.article-list-title > h2


#load-content > div:nth-child(1) > div.article-list-info.content_center > span > a.article-list-cate.content_center > h3


#main-container > div.main-content.mag-content.clearfix > div > div.col-md-8 > article:nth-child(2) > header > h3 > a
#main-container > div.main-content.mag-content.clearfix > div > div.col-md-8 > article:nth-child(2) > header > p > a
#main-container > div.main-content.mag-content.clearfix > div > div.col-md-8 > article:nth-child(8) > header > p > span
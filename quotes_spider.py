from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/2',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/3',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/4',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/5',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/6',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/7',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/8',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/9',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/10',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/11',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/12',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/13',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/14',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/15',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/16',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/17',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/18',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/19',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/20',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/21',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/22',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/23',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/24',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/25',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/26',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/27',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/28',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/29',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/30',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/31',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/32',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/33',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/34',
            'https://pta.trunojoyo.ac.id/c_search/byprod/10/35',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range (1,6):
        
            for PTA in response.css('#content_journal > ul'):
                yield{
                    'Judul Jurnal':PTA.css('li:nth-child('+ str(i) +') > div:nth-child(1) > a::text').extract(),
                    'Penulis':PTA.css('li:nth-child('+ str(i) +') > div:nth-child(1) > div:nth-child(2) > span::text').extract()
                }            
            
        
        
        
        
        
        
        
        


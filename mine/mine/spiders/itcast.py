import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    #allowed_domains = ("edu.cn")#搜索的域名范围，爬虫约束的区域
    start_urls = ("http://192.168.1.90:28073/web/export/xls2",)#爬取URL的列表，所要爬取的网址

    def parse(self, response):
        filename = "t.html"
        open(filename, 'wb').write(response.body)
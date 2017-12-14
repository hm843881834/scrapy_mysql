import scrapy
from tutorial.items import WebcrawlerScrapyItem #导入item对应的类

class BookSpider(scrapy.Spider):
    # name属性，每一个爬虫的唯一标识
    name = "books"

    allowed_domains = ["floor.0731fdc.com"]  # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页

    start_urls = ["http://floor.0731fdc.com/search.php"]  # 开始爬取的地址

    # 该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    def parse(self, response):
        all_urls = response.xpath('//li[@class="floorname"]//@href').extract()

        for url in all_urls:
            item = WebcrawlerScrapyItem()  # 实例item（具体定义的item类）,将要保存的值放到事先声明的item属性中
            item['url'] = url
            yield item  # 返回item,这时会自定解析item
'''
        urllib.urlretrieve(realUrl, path)  # 接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径

            all_urls = se.xpath("//a/@href").extract()  # 提取界面所有的url
            for url in all_urls:
                if url.startswith("/fengjing/1920x1080/"):  # 若是满足定义的条件，继续爬取
                    yield Request("http://desk.zol.com.cn" + url, callback=self.parse)
'''
# scrapy crawl [options] <spider> 跑spider的命令
import scrapy
from lxml import etree
from douban.items import DoubanItem  # 导入items.py中定义的item类格式进行封装


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # 测试地址，user agent 以及 IP
    # allowed_domains=['httpbin.org']
    # start_urls=['http://httpbin.org/get']

    # 正式地址
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']  # 框架自动从这里开始发送请求


    def parse(self, response):
        # print(response.text)
        html = etree.HTML(response.text)  # 用etree来解析
        li_list = html.xpath("//ol[@class='grid_view']/li")  # 用Xpath来查找元素
        # item_list=[]
        for li in li_list:
            item = DoubanItem()  # 导入items.py中定义的item类格式进行封装
            item['em'] = li.xpath(".//em/text()")[0]  # 注意，通过xpath返回的始终是一个list.需要处理后才能用
            item['title'] = li.xpath(".//img/@src")[0]
            item['img'] = li.xpath(".//span[@class='title']/text()")[0]
            item['comment'] = li.xpath(".//div[@class='star']/span/text()")[-1]
            # item_list.append(item)
            yield item  # 利用yield返回一个迭代对象 这里是产生一个item并继续往下执行下一个yield
            # print('打印for循环中的记录', item)

        try:  # 最后一页没有href值，会抛异常，所以用try来处理
            next_page = html.xpath("//span[@class='next']/a/@href")[0]  # 在当前页面获取下一页的地址
            print("一页循环完毕，进入下一页" + "-" * 100)
            # 利用Request手动发送请求， 回调函数调用自己去访问下一页形成递归循环算法
            # 注意callback=self.parse不能加括号，代表把函数的地址赋值给callback.如果加括号，代表把函数的执行结果给callback.
            yield scrapy.Request(url='https://movie.douban.com/top250' + next_page, callback=self.parse)
        except:
            print("下载完毕！")



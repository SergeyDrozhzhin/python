from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, spiders

import crawler.spiders.news_spider as qq

print('Меню')
print('Для того чтобы загрузить новости, нажмите 1')

number= int(input())


def menu1():

    #
    # spider = qq.NewsSpider()
    # crawler = Crawler(Settings())
    # crawler.configure()
    # crawler.crawl(spider)
    # crawler.start()
#log.start()
 #   reactor.run()  # the script will block here





if number ==1:
    menu1()

# описываем паука
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import NewsItemLoader, NewsItem
from scrapy.contrib.loader.processor import Compose, MapCompose
from w3lib.html import replace_escape_chars


class NewsSpider(CrawlSpider): #класс паука.
    name = 'spider'
    allowed_domains = ['fontanka.ru'] #спико тех доменов, за которые не должен выходить паучок
    start_urls = ['http://www.fontanka.ru/24hours_news.html'] #список тех урлов, с которых начнёт работать нащ паучок
    # за пределы не пойдет этого домена
#rules определяет правила поведения для гашего паучка
    #описывает поведение перехода по всем ссылкам. он переходит автоматически, но можно ввести некоторые ограничения
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="calendar-widget"]'], #паук будет ходить по данному икспасу и выберет всю информацию
                #restrict_xpaths=['//div[@class="container footer-stick"]'
                #			 '//div[@class="searchable-container"]'],
                 allow=r'http://www.fontanka.ru/\d+/\d+' #здесь указываем те урлы, по которым должен ходить наш паучок

            ), 'parse_item'
        ),
    )

    def parse_item(self, response): #краулинг страниц. респонс
        selector = Selector(response) # принимает объект респонс
        l = NewsItemLoader(NewsItem(), selector)
        l.default_output_processor= MapCompose(lambda v: v.strip(), replace_escape_chars)
        l.add_value('url', response.url)
        l.add_xpath('title', '//h1[@class="article_title"]/text()')
        l.add_xpath('date', '//div[@class="article_date fll"]/text()')
        l.add_xpath('tag', '//div[@class="article_cat"]//a//span[@class="light"]/text()')
        l.add_xpath('description', '//div[@class="article_desc"]//div[@class="article_fulltext"]/p/text()')
        #            '//div[@class="search_item"]//div[@class="search_top clr-a"]//div[@class="date flr"]/text()')
        #l.add_xpath('tag',
        #           '//div[@class="search_item"]//div[@class="search_top clr-a"]//div[@class="label flr"]/a/text()')
        #l.add_xpath('description', '//div[@class="search_item"]//div[@class="search_bottom clr-a"]//a/text()')

        return l.load_item()

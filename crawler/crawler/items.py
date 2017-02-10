# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from w3lib.html import replace_escape_chars

class NewsItem(scrapy.Item):
	url= scrapy.Field()
	title= scrapy.Field()#Здесь определяем сущности, которые будем собирать
	date = scrapy.Field()
	tag = scrapy.Field()
	description= scrapy.Field()

	pass

class NewsItemLoader(ItemLoader): #определгить для конкретного обработки наших данных он наследуется от класса итем лодер
	#обрабаотывает всё нашу информацию, приводит данные в нужный вид
	#takefirst()
	#префикс ин и оут. обработать данные на входе и на выходе
	url_out= TakeFirst()
	title_out=TakeFirst()
	date_in=MapCompose(lambda f: f.strip(), replace_escape_chars)
	date_out=TakeFirst()
	#description_in= Join()
	description_in=MapCompose(lambda z: z.strip('\n').strip('\r').strip('\t'))
	description_out=Join()
	tag_out=TakeFirst()

	pass
 #для обработки данных
	
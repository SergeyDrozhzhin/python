# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.conf import settings

# from scrapy.contrib.exporter import CsvItemExporter

import json
from scrapy.exporters import JsonItemExporter


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open("news.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

#
# class JsonWriterPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open('news.json', 'w')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#
#         line = json.dumps(dict(item)) +','+'\n'
#         self.file.write(line)
#         return item


# class CsvPipeline(object):
#     def __init__(self):
#         self.file = open("news.csv", 'wb')
#         self.exporter = CsvItemExporter(self.file, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
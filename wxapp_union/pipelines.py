# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WxappUnionPipeline:
    def open_spider(self,spider):
        self.file = open('output.text','w')
    def process_item(self, item, spider):
        self.file.write(str(item))
        return item

    def close_spider(self, spider):
        self.file.close()

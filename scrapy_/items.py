
import scrapy
from scrapy.loader.processors import TakeFirst  # string type instead of list in pipeline after yield


class ArticleItem(scrapy.Item):
    counter = scrapy.Field(output_processor=TakeFirst())  # "string" type
    url = scrapy.Field(output_processor=TakeFirst())  # "string" type
    title = scrapy.Field(output_processor=TakeFirst())  # "string" type
    date = scrapy.Field(output_processor=TakeFirst())  # "string" type
    views = scrapy.Field(output_processor=TakeFirst())  # "string" type
    image = scrapy.Field(output_processor=TakeFirst())  # "string" type
    content = scrapy.Field()  # [list] of lines of contents


class CategoryItem(scrapy.Item):
    counter = scrapy.Field(output_processor=TakeFirst())  # "string" type
    url = scrapy.Field(output_processor=TakeFirst())  # "string" type
    category = scrapy.Field(output_processor=TakeFirst())  # "string" type
    title = scrapy.Field(output_processor=TakeFirst())  # "string" type
    date = scrapy.Field(output_processor=TakeFirst())  # "string" type
    views = scrapy.Field(output_processor=TakeFirst())  # "string" type
    image = scrapy.Field(output_processor=TakeFirst())  # "string" type
    content = scrapy.Field()  # [list] of lines of contents

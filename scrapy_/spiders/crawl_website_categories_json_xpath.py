
import time
import json
import scrapy
import random
import datetime
import dateparser
from items import CategoryItem
from scrapy.loader import ItemLoader
from model.xpath_model import XpathModel
from model.website_model import WebsiteModel
from model.category_model import CategoryModel


class CrawlWebsiteCategoriesJsonXpath(scrapy.Spider):  # [ -- Requests Sent by order and Receive Responses (to crawl) not the same order -- ] -=-=->> -=-=->> -=-=->> -=-=->> -=-=->> -=-=->>>> (- - [DW] - -)
    name = "crawl_website_categories_json_xpath"  # in one website and more than categories

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.move_to_next_page = True
        self.category_type = str()
        self.counter = -1

        json_file = self.get_json_data()

        self.website_info = WebsiteModel(website_name=json_file['website_name'],
                                         description=json_file['description'],
                                         xpath=json_file['xpath'])

        self.xpath = XpathModel(next_page=self.website_info.xpath['next_page'], articles=self.website_info.xpath['articles'],
                                article_url=self.website_info.xpath['article_url'], article_date=self.website_info.xpath['article_date'],
                                title=self.website_info.xpath['title'], date=self.website_info.xpath['date'],
                                views=self.website_info.xpath['views'], image=self.website_info.xpath['image'],
                                content=self.website_info.xpath['content'])

    def start_requests(self):
        for start_category in self.website_info.description:  # more than category (urls & names)
            category_info = CategoryModel(category_type=start_category['category_type'],
                                          category_url=start_category['category_url'],
                                          depth=start_category['depth'])
            yield scrapy.Request(url=category_info.url, callback=self.parse, meta={'category': category_info.type, 'depth_': category_info.depth})  # 'depth' defined in _init_ class Meta, use instead 'depth_'

    def get_json_data(self):
        file = open('first_website.json', 'r')
        string = file.read()
        json_file = json.loads(string)
        return json_file

    def time_converter(self, time_text):
        date_formats_ymd = dateparser.parse(time_text,
                                            date_formats=['%Y-%m-%d %H:%M:%S'],
                                            languages=['en', 'ar'],
                                            settings={'DATE_ORDER': 'MDY', 'TIMEZONE': '+0200'})
        if date_formats_ymd is None:
            timestamp = None
        else:
            timestamp = datetime.datetime.timestamp(date_formats_ymd)
            timestamp = str(timestamp).split('.')[0] + '000'
        return timestamp

    def parse(self, response, **kwargs):  # scroll pages  ( response : is url to first page )

        for item in self.crawling_single_page(response):  # crawling page [url in response]
            yield item

        next_page = response.xpath(self.xpath.next_page)
        if next_page:
            next_url_page = next_page.attrib['href']
            time.sleep(random.uniform(0.2, 0.5))
            if self.move_to_next_page and self.category_type == response.meta['category']:  # (False) if cross the Depth in category
                yield scrapy.Request(url=next_url_page, callback=self.parse, meta={'category': response.meta['category'], 'depth_': response.meta['depth_']})  # To Open (URL)  [-Do'nt put (Yield'request') in (loop'for')-] && [-((DW))- open page By page (all pages have the same format to move to next page) -((DW))-]

    def crawling_single_page(self, response):  # scroll articles
        articles = response.xpath(self.xpath.articles)
        category = response.meta['category']
        depth = self.time_converter(response.meta['depth_'])
        print(f'check articles =({len(articles)}) in page () in category({category}).')

        for index, article in enumerate(articles):
            article_url = article.xpath(self.xpath.article_url).attrib['href']
            article_date = article.xpath(self.xpath.article_date).attrib['datetime']

            article_timestamp = self.time_converter(article_date)

            if article_timestamp > depth:
                self.move_to_next_page = True
                self.category_type = response.meta['category']
                print(f'category({category}) -- page() -- article({index}) -- date({article_date}) -- url({article_url}) -- Send request to crawl later --->')
                time.sleep(random.uniform(0.2, 0.5))
                yield scrapy.Request(url=article_url, callback=self.crawling_single_article, meta={'category': self.category_type})  # collection all articles urls then crawling all [-((DW))- we can't move from article to another like pages -((DW))-]
            else:
                self.move_to_next_page = False
                self.category_type = response.meta['category']
                print(f'cross limit of Depth [End] in category({self.category_type}), Start crawling responses of articles url ...')
                break

    def crawling_single_article(self, response):
        self.counter += 1
        url = response.url
        title = response.xpath(self.xpath.title).get()
        date = response.xpath(self.xpath.date).attrib['datetime']
        content = response.xpath(self.xpath.content).getall()
        views = response.xpath(self.xpath.views).get()
        image = response.xpath(self.xpath.image).attrib['src']

        item_loader = ItemLoader(item=CategoryItem())
        item_loader.add_value('counter', self.counter)
        item_loader.add_value('url', url)
        item_loader.add_value('category', response.meta['category'])
        item_loader.add_value('title', title)
        item_loader.add_value('date', date)
        item_loader.add_value('views', views)
        item_loader.add_value('image', image)
        item_loader.add_value('content', content)

        time.sleep(random.uniform(0.2, 0.5))
        yield item_loader.load_item()  # call [pipeline] to call [processor]

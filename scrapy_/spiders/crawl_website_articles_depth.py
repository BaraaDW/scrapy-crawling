
import time
import scrapy
import datetime
import dateparser
from items import ArticleItem
from scrapy.loader import ItemLoader


class CrawlWebsite(scrapy.Spider):  # [ -- Requests Sent by order and Receive Responses (to crawl) not the same order -- ] -=-=->> -=-=->> -=-=->> -=-=->> -=-=->> -=-=->>>> (- - [DW] - -)
    name = "crawl_website_articles"  # in one website

    def start_requests(self):
        yield scrapy.Request(url=f'https://{self.website}/main/articles', callback=self.parse)  # To Open (URL) = 'https://nasainarabic.net/main/articles'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.move_to_next_page = True
        self.page_number = -1
        self.counter = -1
        self.depth = self.time_converter('2022-01-13 16:02:00')
        if 'website' in kwargs:
            self.website = kwargs['website']

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
        self.page_number += 1

        for item in self.crawling_single_page(response):  # crawling page [url in response]
            yield item

        next_page = response.xpath('//li[@class="active"]/following-sibling::li/a[@href]')
        if next_page:
            next_url_page = next_page.attrib['href']
            time.sleep(1)
            if self.move_to_next_page:  # (False) if cross the Depth
                yield scrapy.Request(url=next_url_page, callback=self.parse)  # To Open (URL)  [-Do'nt put (Yield'request') in (loop'for')-] && [-((DW))- open page By page (all pages have the same format to move to next page) -((DW))-]

    def crawling_single_page(self, response):  # scroll articles
        articles = response.xpath('//section[@class="articles"]/article')
        print(f'check articles =({len(articles)}) in page ({self.page_number}).')

        for index, article in enumerate(articles):
            article_url = article.xpath('.//header/*/a[@href]').attrib['href']
            article_date = article.xpath('.//time[@datetime]').attrib['datetime']

            article_timestamp = self.time_converter(article_date)
            if article_timestamp > self.depth:
                print(f'website({self.website}) -- page({self.page_number}) -- article({index}) -- date({article_date}) -- url({article_url}) -- Send request to crawl later --->')
                time.sleep(1)
                yield scrapy.Request(url=article_url, callback=self.crawling_single_article)  # collection all articles urls then crawling all [-((DW))- we can't move from article to another like pages -((DW))-]
            else:
                print('cross limit of Depth [End], Start crawling responses of articles url ...')
                self.move_to_next_page = False
                break

    def crawling_single_article(self, response):
        self.counter += 1
        url = response.url
        title = response.xpath('//header[@class="page-header"]/*/text()').get()
        date = response.xpath('//ul[@class="list-inline text-muted"]/li[1]//time[@datetime]').attrib['datetime']
        views = response.xpath('//ul[@class="list-inline text-muted"]/li[2]/text()').get()
        image = response.xpath('//div[@itemprop="image"]/img[@src]').attrib['src']
        content = response.xpath('//div[@itemprop="articleBody"]//text()').getall()

        item_loader = ItemLoader(item=ArticleItem())
        item_loader.add_value('counter', self.counter)
        item_loader.add_value('url', url)
        item_loader.add_value('title', title)
        item_loader.add_value('date', date)
        item_loader.add_value('views', views)
        item_loader.add_value('image', image)
        item_loader.add_value('content', content)

        time.sleep(1)
        yield item_loader.load_item()  # call [pipeline] to call [processor]

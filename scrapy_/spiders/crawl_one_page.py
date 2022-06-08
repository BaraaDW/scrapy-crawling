import scrapy
from items import ArticleItem
from scrapy.loader import ItemLoader


class OneNasa(scrapy.Spider):
    name = "one_page"  # in one website
    # start_urls = ['https://alwatan.ae/', 'https://nasainarabic.net/']  # ______more than ((website))______

    def start_requests(self):
        yield scrapy.Request(url=f'https://{self.website}/', callback=self.parse)  # To Open (URL)
        # for start_url in self.start_urls:  # ______more than ((website))______
        #     yield scrapy.Request(url=start_url, callback=self.parse)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'website' in kwargs:
            self.website = kwargs['website']

    def parse(self, response, **kwargs):
        see_all_articles = response.xpath('//section[@class="articles"]/ancestor::div[1]/a[@href]').attrib['href']
        yield scrapy.Request(see_all_articles, callback=self.parse_target)  # To Open (URL)

    def parse_target(self, response):
        articles = response.xpath('//header[not(@class)]/*/a[@href]')
        print(f'We Found ({len(articles)}) of articles.')

        for index, article in enumerate(articles):
            article_url = article.attrib['href']
            print(f'({index})Open url & crawl article ({article_url})')
            yield scrapy.Request(url=article_url, callback=self.crawling_article)  # To Open (URL)

    def crawling_article(self, response):
        url = response.url
        title = response.xpath('//header[@class="page-header"]/*/text()').get()
        date = response.xpath('//ul[@class="list-inline text-muted"]/li[1]//time[@datetime]').attrib['datetime']
        views = response.xpath('//ul[@class="list-inline text-muted"]/li[2]/text()').get()
        image = response.xpath('//div[@itemprop="image"]/img[@src]').attrib['src']
        content = response.xpath('//div[@itemprop="articleBody"]//text()').getall()

        item_loader = ItemLoader(item=ArticleItem())
        item_loader.add_value('url', url)
        item_loader.add_value('title', title)
        item_loader.add_value('date', date)
        item_loader.add_value('views', views)
        item_loader.add_value('image', image)
        item_loader.add_value('content', content)

        yield item_loader.load_item()  # call [pipeline] to call [processor]

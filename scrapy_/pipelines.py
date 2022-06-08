
from spiders.crawl_website_categories_json_xpath import CrawlWebsiteCategoriesJsonXpath
from spiders.crawl_two_websites_categories_json_xpath import CrawlTwoWebsiteCategoriesJsonXpath
from spiders.crawl_website_categories import CrawlWebsiteCategories
from category_processor import CategoryProcessor
from article_processor import ArticleProcessor
from items import ArticleItem
import json
import os


class ScrapyPipeline:

    def process_item(self, item, spider):

        if not hasattr(self, 'articles'):
            self.articles = list()

        if isinstance(item, ArticleItem):
            ArticleProcessor().insert(item)

        elif spider.name == CrawlWebsiteCategories.name:
            CategoryProcessor.insert(item)

        elif spider.name == CrawlWebsiteCategoriesJsonXpath.name or spider.name == CrawlTwoWebsiteCategoriesJsonXpath.name:
            article = CategoryProcessor.insert(item)
            self.articles.append(article)
        return item

    def close_spider(self, spider):
        if spider.name == CrawlWebsiteCategoriesJsonXpath.name or spider.name == CrawlTwoWebsiteCategoriesJsonXpath.name:

            category_file = os.path.abspath(f"category.json")
            if os.path.exists(category_file):
                os.remove(category_file)

            with open('category.json', 'a') as file:
                print(f'we crawled --({len(self.articles)})-- article.')
                file.write(json.dumps(self.articles))
                file.close()

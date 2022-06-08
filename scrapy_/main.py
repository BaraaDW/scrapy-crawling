"""Main script for debugging purposes"""
from scrapy import cmdline

cmdline.execute("scrapy crawl crawl_two_websites_categories_json_xpath -a website=nasainarabic.net".split())

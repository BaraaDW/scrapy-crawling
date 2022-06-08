import json


class ArticleProcessor:
    """ Manage all page's operations """

    @staticmethod
    def insert(article_item):
        print('---------------[-> Article Processor <-]---------------')
        counter = int()
        url = str()
        title = str()
        date = str()
        views = str()
        image = str()
        content = str()

        if 'counter' in article_item:
            counter = article_item['counter']

        if 'url' in article_item:
            url = article_item['url']

        if 'title' in article_item:
            title = article_item['title']

        if 'date' in article_item:
            date = article_item['date']

        if 'views' in article_item:
            views = article_item['views']

        if 'image' in article_item:
            image = article_item['image']

        if 'content' in article_item:
            lines = article_item['content']
            content = ''
            for line in lines:
                content = content + line

        article = dict(counter=counter, url=url, title=title, date=date, views=views, image=image, content=content)
        print(dict(counter=counter, url=url))

        # with open('NASA.json', 'a') as file:
        #     file.write(json.dumps(article))
        #     file.write(",")
        #     file.close()


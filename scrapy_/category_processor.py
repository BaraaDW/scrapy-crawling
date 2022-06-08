import json


class CategoryProcessor:
    """ Manage all page's operations """

    @staticmethod
    def insert(category_item):
        print('---------------[-> Category Processor <-]---------------')
        counter = int()
        url = str()
        category = str()
        title = str()
        date = str()
        views = str()
        image = str()
        content = str()

        if 'counter' in category_item:
            counter = category_item['counter']

        if 'url' in category_item:
            url = category_item['url']

        if 'category' in category_item:
            category = category_item['category']

        if 'title' in category_item:
            title = category_item['title']

        if 'date' in category_item:
            date = category_item['date']

        if 'views' in category_item:
            views = category_item['views']

        if 'image' in category_item:
            image = category_item['image']

        if 'content' in category_item:
            lines = category_item['content']
            content = ' '.join(lines)
            content = content.replace('\n', ' ')

        article = dict(counter=counter, url=url, category=category, title=title, date=date, views=views, image=image, content=content)
        short_article = dict(counter=counter, url=url, category=category)
        print(short_article)
        return short_article

        # with open('category.json', 'a') as file:
        #     file.write(json.dumps(short_article))
        #     # file.write(",")
        #     file.close()

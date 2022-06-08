from model._base_model import BaseModel


class XpathModel(BaseModel):

    def __init__(self, next_page=None, articles=None, article_url=None, article_date=None, title=None, date=None, views=None, image=None, content=None):
        self.next_page = next_page
        self.articles = articles
        self.article_url = article_url
        self.article_date = article_date
        self.title = title
        self.date = date
        self.views = views
        self.image = image
        self.content = content

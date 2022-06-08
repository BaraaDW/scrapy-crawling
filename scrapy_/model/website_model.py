from model._base_model import BaseModel


class WebsiteModel(BaseModel):

    def __init__(self, website_name=None, description=None, xpath=None):
        self.website_name = website_name
        self.description = description
        self.xpath = xpath

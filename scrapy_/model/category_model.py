from model._base_model import BaseModel


class CategoryModel(BaseModel):

    def __init__(self, category_type=None, category_url=None, depth=None):
        self.type = category_type
        self.url = category_url
        self.depth = depth

import json
from datetime import datetime


class BaseModel:
    def json(self) -> str:
        return json.dumps(self, indent=4,
                          default=lambda o: o.__dict__ if not isinstance(o, datetime) else dict(year=o.year,
                                                                                                month=o.month,
                                                                                                day=o.day))

    def __str__(self):
        return self.json()

    def __repr__(self):
        return self.json()

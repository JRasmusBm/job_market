import mongoengine as mongoengine
from datetime import datetime
from mongoengine import connect
connect()

class Offer(mongoengine.Document):
    title = mongoengine.StringField(required=True)
    company = mongoengine.StringField(required=True)
    location = mongoengine.StringField(required=True)
    link = mongoengine.StringField(required=True, unique=True)

    meta = {
        "db-alias": "core",
        "collection": "offers",
        "indexes": [
            "title",
            "company",
            "location",
            "link",
        ]
    }

    def __str__(self):
        return f"""
            Title: {self.title}
            Company: {self.company}
            Location: {self.location}
            Link: {self.link}
            """

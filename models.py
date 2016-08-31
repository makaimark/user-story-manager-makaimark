from peewee import *
import config
from flask import Flask, request


app = Flask('Tweetcool server')
DATABASE = 'sprint_reporter_app.db'


# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase(config.dbname, user=config.name)


class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db

class UserStory(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = CharField()
    estimation = IntegerField()
    status = CharField()

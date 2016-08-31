# This script can create the database tables based on your models

from models import *

db.connect()
# List the tables here what you want to create...

print("Drop table")  # Drop all tables automatic.
db.drop_tables([UserStory], safe=True)
print("Create table")  # Create all tables automatic.
db.create_tables([UserStory], safe=True)

from app import db
from models import *

# create the database and db tables
db.create_all()
# insert
db.session.add(BlogPost("Good","I\'m good."))
db.session.add(BlogPost("Well","I\'m well."))
db.session.add(BlogPost("Test","Shell Test."))


# commit the changes
db.session.commit()

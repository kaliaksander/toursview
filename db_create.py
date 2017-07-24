from app import db
from models import *

# create the database and db tables
db.create_all()
# insert
db.session.add(BlogPost("1","aaaa"))
db.session.add(BlogPost("2","bbbb"))
db.session.add(BlogPost("3","cccc"))


# commit the changes
db.session.commit()

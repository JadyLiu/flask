from app import db
from models import BlogPost

# create the database and the db tables
db.create_all()

# insert 
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("postgrs", "we setup a local postgres instances"))

# commit the changes
db.session.commit()
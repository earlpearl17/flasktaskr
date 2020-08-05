# project / db_create.py

from views import db
from models import Task
from datetime import date

#import pdb

#pdb.set_trace()

# create the database and the db table
db.create_all()

# insert data
#db.session.add(Task("Finish SQLAlchemy tutorial", date(2020, 8, 4), 10, 1))
#db.session.add(Task("Finish Real Python Part 2", date(2020, 9, 17), 10, 1))

# commit the changes
db.session.commit()

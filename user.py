from models import *
from sqlalchemy import and_

def given_review(username, title):
    if(username == None or title == None):
        return False
    else:
        data = ReviewRecord.query.filter(and_(ReviewRecord.username == username, ReviewRecord.title == all_book.title)).all()
        if(len(data) > 0):
            return True
        else:
            return False


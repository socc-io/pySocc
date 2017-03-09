from app import db
from app.Model.StudyModel import Study, StudyIssue

def get(id) :
    return db.session.query(Study).get(id)

def create(owner_id, **args) :
    obj = Study(owner_id=owner_id, **args)
    db.session.add(obj)
    db.session.commit()
    return obj

def delete(obj) :
    db.session.delete(obj)
    db.session.commit()

def checkName(name) :
    return True if db.session.query(Study).filter(Study.name == name).first() else False

def getIssue(id) :
    return db.session.query(StudyIssue).get(id)

def createIssue(**args) :
    obj = StudyIssue(**args)
    db.session.add(obj)
    db.session.commit()
    return obj

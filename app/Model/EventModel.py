from app import db
from datetime import datetime, timedelta

event_attendance = db.Table('event_attendance',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

class Event(db.Model):
	"""Event Model"""
	__tablename__ = 'event'
	id = db.Column(db.Integer, primary_key=True)
	writer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	study_id = db.Column(db.Integer, db.ForeignKey('study.id'))
	date = db.Column(db.DateTime)
	content = db.Column(db.Text)

	writer = db.relationship('User')
	study = db.relationship('Study')
	attending_users = db.relationship('User', secondary=event_attendance)
	def __init__(self, writer_id, date, content='', study_id=None):
		self.writer_id = writer_id
		self.date = datetime.strptime(date, '%Y-%m-%d')
		self.content = content
		self.study_id = study_id
	def __repr__(self):
		return '<Event date:{}, content: {}>'.format(self.date, self.content)
	def dict(self, join=False) :
		base = {
			'writer_id': self.writer_id,
			'date': self.date,
			'content': self.content
		}
		if join :
			joined = {
				'writer': writer.dict()
			}
			base = dict(base, **joined)
		return base
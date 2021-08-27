from db import db
import datetime


class PublicationModel(db.Model):
    __tablename__ = 'publics'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    public_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
    def json(self):
       return {
           "id": self.id, 
           "title": self.title, 
           "content": self.content, 
           "public_date": self.public_date.strftime("%Y-%m-%d %H:%M:%S")
           }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() 
       
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  
    
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
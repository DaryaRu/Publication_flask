from db import db

class UserModel(db.Model):
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String) 
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)

    def __init__(self, username, password, name, surname):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()    

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
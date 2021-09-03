from db import db

class LikeModel(db.Model):
    __tablename__ = 'likes'

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    publication_id = db.Column(db.Integer, db.ForeignKey("publications.id"), primary_key=True)

    def __init__(self, user_id, publication_id):
        self.user_id = user_id
        self.publication_id = publication_id

    def save_like_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_like_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_like(cls, user_id, publication_id):
        return cls.query.filter_by(user_id=user_id, publication_id=publication_id).first()

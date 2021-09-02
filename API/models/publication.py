from db import db
import datetime


class PublicationModel(db.Model):
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    public_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    rubric_id = db.Column(db.Integer, db.ForeignKey(
        "rubrics.id"), nullable=False)
    rubric = db.relationship("RubricModel", back_populates="publications")

    def __init__(self, title, content, rubric_id):
        self.title = title
        self.content = content
        self.rubric_id = rubric_id

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "public_date": self.public_date.strftime("%Y-%m-%d %H:%M:%S"),
            "rubric_id": self.rubric_id
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

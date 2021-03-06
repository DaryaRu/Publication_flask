from models.db import db


class RubricModel(db.Model):
    __tablename__ = 'rubrics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    publications = db.relationship(
        "PublicationModel", lazy="dynamic",
        back_populates="rubric",
        cascade="all, delete, delete-orphan")

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"id": self.id, "name": self.name, "publications": [publication.json() for publication in self.publications.all()]}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

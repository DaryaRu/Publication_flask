from sqlalchemy.orm import relationship
from sqlalchemy import and_
from models.db import db
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

    users = relationship("UserModel", secondary="likes",
                         back_populates="publications")

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
            "rubric_id": self.rubric_id,
            "likes_count": len(self.users)
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_paged(cls, query):
        page = query["page"]
        page_size = query["page_size"]
        title = query["title"]
        rubric_id = query["rubric_id"]
        content = query["content"]

        filters_list = []

        if(title):
            filters_list.append(PublicationModel.title.contains(title))

        if(content):
            filters_list.append(PublicationModel.content.contains(content))    

        if(rubric_id):
            filters_list.append(PublicationModel.rubric_id.like(rubric_id))

        return cls.query.filter(
            and_(*filters_list)
        ).paginate(page, page_size, False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

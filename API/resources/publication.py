from flask_restful import Resource, reqparse
from models.publication import PublicationModel
# import datetime


class Publication(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("title", type=str, required=True,
                        help="This field cannot be left blank")
    parser.add_argument("content", type=str, required=True,
                        help="This field cannot be left blank")

    def get(self, id):
        publication = PublicationModel.find_by_id(id)
        if publication:
            return publication.json()
        return {"message": "Public is not found"}, 404

    def delete(self, id):
        publication = PublicationModel.find_by_id(id)
        if publication:
            publication.delete_from_db()

        return {"message": "Publication deleted"}

    def put(self, id):

        data = Publication.parser.parse_args()

        publication = PublicationModel.find_by_id(id)

        if publication is None:
            return {"message": "not found"}
        else:
            publication.title = data['title']
            publication.content = data['content']
            publication.save_to_db()
       

        return publication.json()


class PublicationList(Resource):
    def get(self):
        return {"publications": [publication.json() for publication in PublicationModel.query.all()]}

    def post(self):
        data = Publication.parser.parse_args()
        publication = PublicationModel(data['title'], data['content'])

        
        try:
            publication.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return publication.json(), 201

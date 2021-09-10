from flask_restful import Resource, reqparse
from models.publication import PublicationModel
from flask_jwt import jwt_required
from parsers.publications import publication_create_parser, publication_list_parser


class Publication(Resource):
    
    @jwt_required()
    def get(self, id):
        publication = PublicationModel.find_by_id(id)

        if publication:
            return publication.json()

        return {"message": "Public is not found"}, 404

    @jwt_required()
    def delete(self, id):
        publication = PublicationModel.find_by_id(id)

        if publication:
            publication.delete_from_db()

        return {"message": "Publication deleted"}

    @jwt_required()
    def put(self, id):
        data = publication_create_parser.parse_args()
        publication = PublicationModel.find_by_id(id)

        if publication is None:
            return {"message": "not found"}
        else:
            publication.title = data['title']
            publication.content = data['content']
            publication.save_to_db()

        return publication.json()


class PublicationList(Resource):
    
    @jwt_required()
    def get(self):
        data = publication_list_parser.parse_args()
        result = PublicationModel.find_paged(data)
        
        return {"pages": result.pages,
                "has_next": result.has_next,
                "publications": [publication.json() for publication in result.items]}

    @jwt_required()
    def post(self):
        data = publication_create_parser.parse_args()
        publication = PublicationModel(
            data['title'], data['content'], data['rubric_id'])

        try:
            publication.save_to_db()
        except:
            return {"message": "An error occurred inserting the publication"}, 500

        return publication.json(), 201

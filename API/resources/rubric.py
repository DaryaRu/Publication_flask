from flask_restful import Resource, reqparse
from models.rubric import RubricModel
from flask_jwt import jwt_required
from parsers.rubric import rubric_create_parser

class Rubric(Resource):
    
    @jwt_required()
    def get(self, id):
        rubric = RubricModel.find_by_id(id)
        
        if rubric:
            return rubric.json()
        
        return {"message":"rubric not found"}, 404
    
    @jwt_required()
    def delete(self, id):
        rubric = RubricModel.find_by_id(id)
        
        if rubric:
            rubric.delete_from_db()

        return {"message": "Rubric deleted"}

    @jwt_required()
    def put(self, id):
        data = rubric_create_parser.parse_args()
        rubric = RubricModel.find_by_id(id)

        if rubric is None:
            return {"message": "not found"}
        else:
            rubric.name = data['name']
            rubric.save_to_db()
       
        return rubric.json()

class RubricList(Resource):
    @jwt_required()
    def get(self):
        return {"rubrics": [rubric.json() for rubric in RubricModel.query.all()]}
    
    @jwt_required()
    def post(self):
        data = rubric_create_parser.parse_args()
        rubric = RubricModel(data['name'])
        
        try:
            rubric.save_to_db()
        except:
            return {"message": "An error occurred inserting the rubric"}, 500

        return rubric.json(), 201        

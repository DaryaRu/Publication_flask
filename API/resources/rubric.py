from flask_restful import Resource, reqparse
from models.rubric import RubricModel

class Rubric(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True,
                        help="This field cannot be left blank")

    def get(self, id):
        rubric = RubricModel.find_by_id(id)
        
        if rubric:
            return rubric.json()
        
        return {"message":"rubric not found"}, 404

    def delete(self, id):
        rubric = RubricModel.find_by_id(id)
        
        if rubric:
            rubric.delete_from_db()

        return {"message": "Rubric deleted"}

    def put(self, id):
        data = Rubric.parser.parse_args()
        rubric = RubricModel.find_by_id(id)

        if rubric is None:
            return {"message": "not found"}
        else:
            rubric.name = data['name']
            rubric.save_to_db()
       
        return rubric.json()

class RubricList(Resource):
    def get(self):
        return {"rubrics": [rubric.json() for rubric in RubricModel.query.all()]}

    def post(self):
        data = Rubric.parser.parse_args()
        rubric = RubricModel(data['name'])
        
        try:
            rubric.save_to_db()
        except:
            return {"message": "An error occurred inserting the rubric"}, 500

        return rubric.json(), 201        

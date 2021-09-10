from flask_restful import Resource
from models.user import UserModel
from parsers.user import user_create_parser

class UserRegister(Resource):
                                     
    def post(self):
        data = user_create_parser.parse_args()

        if UserModel.find_by_username(data["username"]) is not None:
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()
        
        return {"message": "User created successfully."}, 201

from flask_restful import Resource, reqparse
from models.like import LikeModel
from models.user import UserModel
from models.publication import PublicationModel

class Like(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=int, required=True)
    parser.add_argument("publication_id", type=int, required=True)

    def post(self):
        data = Like.parser.parse_args()
        user_id = data['user_id']
        publication_id = data['publication_id']

        if UserModel.find_by_id(user_id) is None:
            return {"message": "A user with that id does'n exists"}, 404

        if PublicationModel.find_by_id(publication_id) is None:
            return {"message": "A publication with that id does'n exists"}, 404  

        like_in_table = LikeModel.find_like(user_id, publication_id)

        if like_in_table is None:
            like = LikeModel(user_id, publication_id)
            like.save_like_to_db()
            return {"message": "Your like added"}, 200
        else:
            return {"message": "The like already exists"}, 400

    def delete(self):
        data = Like.parser.parse_args()
        user_id = data['user_id']
        publication_id = data['publication_id']

        if UserModel.find_by_id(user_id) is None:
            return {"message": "A user with that id does'n exists"}, 404

        if PublicationModel.find_by_id(publication_id) is None:
            return {"message": "A publication with that id does'n exists"}, 404

        like = LikeModel.find_like(user_id, publication_id)
        
        if like:
            like.remove_like_from_db()
            return {"message": "Your like deleted"}, 200
        else:
            return {"message": "The like doesn't exist"}, 404    

from flask_jwt import jwt_required, current_identity
from flask_restful import Resource
from models.like import LikeModel


class Favorites(Resource):

    @jwt_required()
    def get(self):
        user_id = current_identity.id
        favorites = LikeModel.get_favorites(user_id)
        return [f.json() for f in favorites]

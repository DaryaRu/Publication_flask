from flask_restful import reqparse

like_create_parser = reqparse.RequestParser()
like_create_parser.add_argument("publication_id", type=int, required=True)
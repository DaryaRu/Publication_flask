from flask_restful import reqparse

rubric_create_parser = reqparse.RequestParser()
rubric_create_parser.add_argument("name", type=str, required=True,
                        help="This field cannot be left blank")
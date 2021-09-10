from flask_restful import reqparse

publication_create_parser = reqparse.RequestParser()
publication_create_parser.add_argument("title", type=str, required=True,
                        help="This field cannot be left blank")
publication_create_parser.add_argument("content", type=str, required=True,
                        help="This field cannot be left blank")
publication_create_parser.add_argument("rubric_id", type=int, required=True,
                        help="Every item needs a rubric id")

publication_list_parser = reqparse.RequestParser()
publication_list_parser.add_argument("page", type=int)
publication_list_parser.add_argument("page_size", type=int)                        
from flask_restful import reqparse

user_create_parser = reqparse.RequestParser()
user_create_parser.add_argument("username", type = str, required = True,
                        help = "This field cannot be blank")
user_create_parser.add_argument("password", type = str, required = True,
                        help = "This field cannot be blank")
user_create_parser.add_argument("name", type = str, required = True,
                        help = "This field cannot be blank")
user_create_parser.add_argument("surname", type = str, required = True,
                        help = "This field cannot be blank") 
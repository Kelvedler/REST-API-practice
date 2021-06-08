import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    for i in 'username', 'password':
        parser.add_argument(i, type=str, required=True, help="{} field cannot be left blank".format(i))

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        else:
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "user created successfully"}, 201

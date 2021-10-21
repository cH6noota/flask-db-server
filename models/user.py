from flask import jsonify, abort, request
from flask_restful import Resource, Api
from datetime import datetime
from database import db
from app import ma

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(255), nullable=False, default="hoge")
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "created_at")
    

users_schema = UserSchema(many=True)


class Userapi(Resource):
    def get(self):
        """
        ユーザを１件取得する
        """
        id = request.args.get('id')
        result = User.query.filter_by(id=id).all()
        if len(result) != 0: 
            return jsonify({"users" : users_schema.dump(result)})
        else:
            # 存在しないユーザIDが指定された
            abort(404)

    def post(self):
        """
        ユーザを登録する
        """
        #ユーザを追加
        print(request.json)
        users = request.json["users"]
        for i in users:
            u  = User(name=i["name"])
            db.session.add(u)
        db.session.commit()

        #正常に登録できたので、HTTP status=204(NO CONTENT)を返す
        return '', 204

    def put(self):
        """
        ユーザを更新する
        """
        id = request.json["id"]
        user = User.query.filter_by(id=id).first()
        
        if user : 
            for key, val in request.json.items():
                setattr(user, key, val)
            db.session.commit()
        else:
            #存在しないユーザIDが指定された場合
            abort(404)

        #正常に更新できたので、HTTP status=204(NO CONTENT)を返す
        return '', 204

    def delete(self):
        """
        ユーザを削除する
        """
        id = request.args.get('id')
        user = User.query.filter_by(id=id).first()
        if user :
            db.session.delete(user)
            db.session.commit()
            return '', 204
        else:
            #存在しないユーザIDが指定された場合
            abort(404)

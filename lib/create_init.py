from models.user  import User
from database import db

def create_init(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        user_create()
        db.session.commit()
    
def user_create():
    # テストデータ
    from test.data.user import users
    for i in users:
        u  = User(name=i["name"])
        db.session.add(u)
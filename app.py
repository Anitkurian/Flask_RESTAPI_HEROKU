from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList
from db import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'#saying that sqlalchemy is running in the root of our project
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False#this tracker track the object that had change the database, we are turning it off, since the bse
#library sqlalchemy have more advanced tracker
app.secret_key='christy'
api=Api(app)

@app.before_first_request
def create_table():
    db.create_all()#we have deleted the create_table file, bcz sqlalchemy will create the table using the decorator

jwt=JWT(app,authenticate,identity)

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
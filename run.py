from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()#we have deleted the create_table file, bcz sqlalchemy will create the table using the decorator
from db import db
class StoreModel(db.Model):
    __tablename__='stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items=db.relationship('ItemModel',lazy='dynamic')#when there are many stores & many itms , so whenever we create a storemodel,
    #we create an object for each item in database,matching the store id.for few items its fine, but for more, it will be expensive
    #so to tell sqlalchemy not to do that,use lazy parameter.
    
    def __init__(self,name):
        self.name=name

    def json(self):
        return {'name':self.name,'items':[items.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
       
  
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


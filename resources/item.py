#import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser =reqparse.RequestParser()#only allows the defined fields to be passed, and not accept any other variable
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
        )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="every item must have a store id"
        )
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            #return item
            return item.json()#becoz the find_by_name function is returning an object
        return {"message": "Item not found"}

    

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':"An item with name '{}'already exists.".format(name)},400
        data=Item.parser.parse_args()
      
        #item={'name':name,'price':data['price']}, beoz its a dictionary, need to be an object
        item=ItemModel(name,data['price'],data['store_id'])
        try:
            #ItemModel.insert(item)
            item.save_to_db()
        except:
            return {"message":"An error occured"}
    
        return item.json(),201
  
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'item deleted'}

        #global items # to tell that we are using the list defined outside the class and its not a local variable
        #items=list(filter(lambda x:x['name']!=name,items))#to update the list with items except the one to be deleted
        #connection =sqlite3.connect('data.db')
        #cursor =connection.cursor()
        #query ="DELETE FROM items WHERE name=?"
        #cursor.execute(query,(name,))

        #connection.commit()
        #connection.close()
        #return {'message':'item deleted'}

    def put(self,name):
        
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
        #updated_item={'name':name,'price':data['price']},bcoz its a dictionary , need to retun an itemmodel object
        #updated_item=ItemModel(name,data['price'])
        if item is None:
            item=ItemModel(name,data['price'],data['store_id'])
           # try:
                #ItemModel.insert(updated_item)
               # updated_item.save_to_db()#updated_item amd item are different here, item is just an entity having a name and price, which is same as that in the database
                #so calling it on update method doesn't chnage anything, whereas updated_item is one having the same,name and diff. price, so calling it on update method, will actually upadte the databse.

            #except:
               # return {"messsage":"An error occured while inserting"}
        else:
            item.price=data['price']
            item.store_id=data['store_id']
            #try:
                #ItemModel.update(updated_item)
                #updated_item.save_to_db()
           # except:
               #  return {"messsage":"An error occured while updating"}
        #return updated_item.json()
        item.save_to_db()
        return item.json()





class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
       # connection =sqlite3.connect('data.db')
        #cursor =connection.cursor()
        #items=[]
        #query ="SELECT * FROM items"
        #result=cursor.execute(query)
        #for row in result:
         #   items.append({'name':row[0],'price':row[1]})
        #connection.close()

        #return {'items':items}
from models.user import UserModel

#users=[
 #   User(1,'Rity','asdf')
#]


#username_mapping={u.username:u for u in users}
#userid_mapping={u.id:u for u in users}
   # {
       # 'id':1,
      #  'username':'Rity',
       # 'password':'asdf'
    #}


#username_mapping={'Rity':
    #{
       # 'id':1,
        #'username':'Rity',
        #'password':'asdf'
    #}

#}

#userid_mapping={1:
 #   {
  #      'id':1,
   #     'username':'Rity',
    #    'password':'asdf'
    #}

#}

def authenticate(username,password):
    user=UserModel.find_by_username(username)
    if user and password==password:
        return user

def identity(payload): #to decode the secret key
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)
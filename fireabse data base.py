import pyrebase

firebaseConfig = {
   #your json here
  }
firebase = pyrebase.initialize_app(firebaseConfig)

# to create a access to database
db = firebase.database()

data = {"name":"shantam"}

data1 = {"name":"rayjan"}
# to create a access to a key and send data
db.child("user").child("res").set("happy")

# to update the data in a key
# str1 = "shantam"
# db.child("user").child("res").update({"name":str1})
# print("done")

# get  data from database

# all = db.child("user").get()
# for u in all.each():
#     data0 =u.val()
# print(data0['name'])

# to remove
#
#db.child('user').child(key).remove()

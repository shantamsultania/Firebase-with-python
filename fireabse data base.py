import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCuf2Xl0QZ4mQFnMNzGM4lT6rrSMsZRuDk",
    'authDomain': "nlpproject-53a72.firebaseapp.com",
    'databaseURL': "https://nlpproject-53a72.firebaseio.com",
    'projectId': "nlpproject-53a72",
    'storageBucket': "nlpproject-53a72.appspot.com",
    'messagingSenderId': "337143249782",
    'appId': "1:337143249782:web:798a5c0c4b8c84b7881857",
    'measurementId': "G-538NHPDSC9"
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

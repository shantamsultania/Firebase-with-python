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

storage = firebase.storage()

# send an image or file

# storage.child("images/new.png").put("imagenew.png")

#get image

storage.child("images/new.png").download("image1.png")


#
# import cv2
#
# img = cv2.imread('image1.png')
# cv2.imshow('image',img)
# cv2.waitKey(0)

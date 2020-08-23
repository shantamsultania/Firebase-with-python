import pyrebase

firebaseConfig = {
  # your json file here
  }
firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

# send an image or file

# storage.child("images/new.png").put("imagenew.png")

#get image

storage.child("images/new.png").download("image1.png")



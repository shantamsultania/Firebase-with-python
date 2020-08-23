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

auth = firebase.auth()
# create a new user
email = "shantam1230@gmail.com"
password = "123456"
# to create a new user
# user = auth.create_user_with_email_and_password(email,password)

# to signin to a account
try:
    signin = auth.sign_in_with_email_and_password(email,password)
    # sent email verification
    auth.send_email_verification(signin['idToken'])
    # to reset the password
    # auth.send_password_reset_email(email)
except:
    print("error")





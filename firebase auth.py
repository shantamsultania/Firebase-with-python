import pyrebase

firebaseConfig = {
#your json
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





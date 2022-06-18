import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import exceptions
import os.path
from operator import itemgetter


app = firebase_admin.initialize_app(
    credentials.Certificate(os.path.join(os.getcwd(), 'justohgay_sdk.json')))
    
db = firestore.client()

ref = db.collection('post')

#CRUD operation
# add a single post
#ref.add({
#    'title': 'title One',
#    'category': 'API',
#    'body': 'In this post we discuss how to build a sophisticated microservice for streaming music that serves an spa'
#})

#authenticate users
def signUp_by_email(**kwargs):
    try:
        auth.get_user_by_email(kwargs['email'])
        print('user does exist')
    except exceptions.NotFoundError:
        uid, display_name, email, email_verified, phone_number, photo_url, password, disabled = itemgetter('uid', 'display_name', 'email', 'email_verified', 'phone_number', 'photo_url', 'password', 'disabled')(kwargs)
        print('user does not exist')
        auth.create_user(uid=uid, display_name=display_name, email=email, email_verified=email_verified, phone_number=phone_number, photo_url=photo_url, password=password, disabled=disabled)
        return auth.generate_email_verification_link(email)
    
    
#link = signUp_by_email(uid='1234', display_name='Allison', email='ogechukwukanu@gmail.com', email_verified=False, phone_number='+2348135277044',photo_url='https://google.com/images/logo.png', password='Allison@2022', disabled=False)
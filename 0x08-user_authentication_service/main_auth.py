#!/usr/bin/env python3
"""
Main file
Testing for Auth class
"""

from auth import Auth
from db import DB

a = Auth()
email = 'user1@test.com'
password = "hashedPwd"
# register_user
user1 = a.register_user(email, password)
print(user1.email)
try:
    duplicate_user = a.register_user(email, password)
except Exception:
    print("already exists")
print('*****')

# valid_login
print(a.valid_login(email, password))
print(a.valid_login('bad_email@gail.com', password))
print(a.valid_login(email, "badpwd"))
print('*****')

# create_session
print(a.create_session(email))
print(user1.session_id)
try:
    a.create_session("bad_email@gmail.com")
except Exception:
    print("email not registered")
try:
    a.create_session(email, "bad_pwd")
except Exception:
    print("wrong password")
print('*****')

# get_user_from_session_id
idd = user1.session_id
userwithid = a.get_user_from_session_id(idd)
print(idd + " of user" + userwithid.email)
userwithid = a.get_user_from_session_id("123")
print(userwithid)
print('*****')

# get_reset_password_token
print("getting reset token of {} with session id of {}".format(user1.email, user1.session_id))
print("generated token is", a.get_reset_password_token(user1.email))
print("user1's reset token is", user1.reset_token)
print('*****')

# update_password
print("reseting pwd", password)
a.update_password(user1.reset_token, "newPWD")
print(a.valid_login(user1.email, "newPWD"))
try:
    a.update_password("123", "newPWD")
except Exception:
    print("Bad token")
print('*****')

# destroy_sessions
a.destroy_session(user1.id)
print("just deleted user1 session id", user1.session_id)
print('*****')

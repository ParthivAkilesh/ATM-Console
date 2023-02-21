from admin import ADMIN
from user import USER

f = 1

while(f):
    
    print("Welcome to Naruto Shippuden One Piece Bank")
    c = int(input("1.Admin\n2.User\nEnter your choice: "))
    if c == 1:
        ad = ADMIN()
        ad.login()
    elif c == 2:
        us = USER()
        us.login()
    else:
        f = 0
          
          

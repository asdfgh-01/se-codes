#database admnin program 9574
log_on_information = {'admin00':'pass123',
                     'hello':'goodbye',
                     'pillow':'fight',
                     'unicorn':'rainbow',
                     'pinkbubbles':'sparkly'}
username = input("enter your username :")
if username in log_on_information:
    password = input("enter your password :")
    if(password==log_on_information['admin00']):
        print("hello "+username+"!you are logged in.")
        print(log_on_information)
    elif(password==log_on_information[username]):
        print("hello "+username+"!you are logged in.")
        change = input("would you like to change your password(y/n) :")
        if change=='n':
            print("thank you!")
        else:
            changed_password = input("enter new password :")
            if (len(changed_password)>8):
                log_on_information[username]=changed_password
                print("password has been changed.")
            else:
                print("must be more than 8 characters in length.")
    else:
        print("invalid password.")
else:
    print("your name is not in the database.")
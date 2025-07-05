email = input("Email : ")
if '@' in email :
    password = input("Enter your password : ")
    if email == "parmarvaidehi437@gmail.com" and password == "vai437dehiparmar" :
        print("WELCOME.")
    elif email == "parmarvaidehi437@gmail.com" and password != "vai437dehiparmar" :
        print("Password Incorrect")
        password = input("Enter your password again : ")
        if password == "vai437dehiparmar" :
            print("Correct.")
        else : 
            print("Still Incorrect.Try Again!!")
    else:
        print("Incorrect Credentials.")
else : 
    print("Check your Email.")

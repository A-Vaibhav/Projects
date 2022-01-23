import re
numbers = "1234567890"
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|org)"  
flag=0
while(flag==0):                                  # loop will run until a valid email id
    email = input("Enter Your Email : ")
    if (email[0] in numbers) or (' ' in email):  # 1st character can't be number & no space allowed
        print("Enter Valid Email")
    else:
        if(re.search(pattern,email)):
            ad = email.index('@')
            username = email[0:ad]
            print(username)
            
            domain = email[ad+1:]
            print(domain)
            flag=1
        else:
            print("Enter Valid Email ")
            
            
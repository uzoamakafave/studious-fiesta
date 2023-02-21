#this is a progarm that controls Uzo's diamond treasury

#get input of the password
#check if input is value password
#do not confirm if password is not in uppercase
#confirm if password is in uppercase
uzo_password = 'UZOAMAKA'

print("Welcome to Uzo's diamond treasury")

password = input("Enter Password: ")

if password == uzo_password:
    print("Access Granted")
else:
    print("Access Refuted")
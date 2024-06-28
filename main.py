import random
import string

characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
print("******** Password Generator ********")
length = int(input("Enter The Length of the Password :- "))
password = ""
for i in range(length):
    password +=random.choice(characters)

print(f"Password = {password}")
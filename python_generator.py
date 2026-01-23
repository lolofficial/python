import random 
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza =  int (input("How much need to be long the password?"))
password = ""
for i in range (lunghezza):
    password = password + random.choice(caratteri)

print(password)
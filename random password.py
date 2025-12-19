import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*~"
length_password=int(input("enter the length of password:"))
a="".join(random.sample(password,length_password))
print(f"your password is{a}")

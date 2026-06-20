import random
import string
print("="*40)
print("PASSWORD GENERATOR")
print("="*40)
upper=int(input("Enter number of Uppercase letters : "))
lower=int(input("Enter number of Lowercase letters : "))
digits=int(input("Enter number of digits : "))
symbols=int(input("Enter number of symbols : "))
password=[]
for i in range(upper):
    password.append(random.choice(string.ascii_uppercase))
for i in range(lower):
    password.append(random.choice(string.ascii_lowercase))
for i in range(digits):
    password.append(random.choice(string.digits))
for i in range(symbols):
    password.append(random.choice(string.punctuation))
random.shuffle(password)
final_password="".join(password)
print("\n"+"="*40)
print("Generated Password:")
print(final_password)
print(list(final_password))
print("="*40)

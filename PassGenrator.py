
import random
def password_generator(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password =''
    for i in range(length):
        x=random.choice(characters)
        password += x # Corrected line: append the random character to the password
    return password
try:
  x=password_generator(8) #can increase size based on our requirement
  print(x)
except Exception as e:
  print ("hey we got error {e} Try again for password generator")

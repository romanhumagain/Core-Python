# To slice the email into two parts i.e username and domain

email = input("Please provide your email address !!")

if '@' in email:
  username = email[:email.index('@')]
  domain  =  email[email.index('@') + 1 :]

  print(f"Your username is {username}")
  print(f"Your domain is {domain}")

else:
  print("Please provide correct email address ")

#EMAIL SLICER CODE IN PYTHON

email = input("Enter your email address: ")

# Extracting username
username = email[:email.index('@')]

# Extracting domain name
domain_name = email[email.index('@')+1:]

# Displaying the username and domain name
print(f"Username: {username}\nDomain Name: {domain_name}")

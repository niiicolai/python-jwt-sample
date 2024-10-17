# A simple helper script to generate 
# a new secret for the .env file

import secrets

print("Copy the following line to your .env file")
print("JWT_SECRET=" + secrets.token_hex(20))

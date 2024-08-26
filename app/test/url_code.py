
import hashlib
import string
import random

def url_to_alphanumeric_code(url, code_length=6):
    # Create an MD5 hash of the URL
    md5_hash = hashlib.md5(url.encode()).hexdigest()
    
    # Take the first 'code_length' characters of the hash
    code = md5_hash[:code_length]
    
    # Ensure the code is alphanumeric (letters and digits only)
    alphanumeric_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(code_length))
    
    return alphanumeric_code

# Get a URL as input
url = input("Enter test URL: ")

# Convert the URL to a 6-character alphanumeric code
alphanumeric_code = url_to_alphanumeric_code(url)
print("Code:", alphanumeric_code)
print("Share the code with the test takers.")

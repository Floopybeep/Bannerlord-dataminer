import hashlib

# with open("binary data.txt", 'rb') as bdata:
#     data = bdata.read()

# Define the text to hash
text = "1410"

# # Convert the text to bytes (UTF-8 encoding)
text_bytes = text.encode('utf-8')

# Compute the SHA-3 hash of the bytes with 1024-bit output
hash_object = hashlib.sha3_512(text_bytes)

# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()

# Print the hash
print(hash_hex)



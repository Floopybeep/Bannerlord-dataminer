from Crypto.Cipher import Blowfish

# key and data to be decrypted
key = bytes("01d3d3dab2d3".encode('utf-8'))


with open("savefile.sav", 'rb') as sav:
    data = sav.read()
# 8120701 bytes

# create the cipher object
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# decrypt the data
decrypted_data = cipher.decrypt(data)

print(decrypted_data)

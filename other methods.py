import _skein

# Load the key
key = "0020B806C000340A7C7664876753888A7577866254C69643C4B647398C95A037"
tweak = "02AEC6240AA74973000000000000000000000000000000000000000023647002"
key = bytes.fromhex(key)
tweak = bytes.fromhex(tweak)

with open("binary data.txt", 'rb') as bdata:
    data = bdata.read()

tf = _skein.threefish(key, tweak)
decrypted_data = tf.decrypt_block(data)

print(decrypted_data)


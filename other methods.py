import struct

with open("savefile.sav", 'rb') as bdata:
    jsonnum = struct.unpack('!HH', bdata.read(4))[0]
    data = bdata.read()
    barray = bytearray(data)

decoded_data = data.decode('unicode_escape')

print(decoded_data)

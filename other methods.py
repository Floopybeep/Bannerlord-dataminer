import struct
import chardet
import codecs

with open("savefile.sav", 'rb') as bdata:
    json_len = struct.unpack('<i', bdata.read(4))[0]
    data = bdata.read()
    # barray = bytearray(data)
    json_content = data[4:json_len].decode('utf-8')

    savedata_content = data[json_len+1:json_len+20]
    # print(chardet.detect(savedata_content))
    # print(savedata_content.decode('iso-8859-6'))
    # print(struct.unpack('c', savedata_content))

# print(savedata_content)
# decoded_data = data.decode('unicode_escape')

# print(decoded_data)

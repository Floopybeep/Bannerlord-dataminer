import chardet
import struct

with open("savefile.sav", 'rb') as sav:
    data = sav.read()

value = struct.unpack_from('<i', data, 0x10)[0]
print(value)
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jonghong0316&logNo=221886820628

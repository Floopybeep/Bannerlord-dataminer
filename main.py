# import chardet
# import struct
#
with open("saveauto2.sav", 'rb') as sav:
    data = sav.read()
#
# value = struct.unpack_from('<i', data, 0x10)[0]
# print(value)

setupfilepath = "D:/Python projects/Bannerlord_dataminer/pyskein-1.0/setup.py"


# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jonghong0316&logNo=221886820628

# Use python "C:\ProgramData\Anaconda3\envs\Bannerlord-dataminer\Scripts\binwalk" as binwalk
# https://stackoverflow.com/questions/1728376/get-a-list-of-all-the-encodings-python-can-encode-to

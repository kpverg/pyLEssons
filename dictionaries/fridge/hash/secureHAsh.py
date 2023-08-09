import hashlib
# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)
python_programm="""for i in range(10):
print(i)
"""
print(python_programm)

# for b in python_programm.encode('utf8'):
#     print(b , chr(b))
originalHash=hashlib.sha256(python_programm.encode('utf8'))
print(f"sha256:{originalHash.hexdigest()}")
python_programm+="print('code Changed')"
# print(python_programm)
newHash=hashlib.sha256(python_programm.encode('utf8'))
print(f"sha256:{newHash.hexdigest()}")


if newHash.hexdigest() == originalHash.hexdigest():
    print("code has naot changed")
else:

    print("code has been changed")
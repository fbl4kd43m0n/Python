import hashlib
 
hasher = hashlib.md5()
with open('myfile', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(hasher.hexdigest())

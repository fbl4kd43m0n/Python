import pefile
pe = pefile.PE("yourfile.exe")
for section in pe.sections:
print "%s\t%s" % (section.Name, section.get_hash_md5())

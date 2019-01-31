import pefile
pe = pefile.PE("somfile.dll")
if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
print "%s" % exp.name

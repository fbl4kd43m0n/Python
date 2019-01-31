import pefile
import sys
pe = pefile.PE(sys.argv[1])
print pe.get_imphash()

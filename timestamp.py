import pefile
import time

pe = pefile.PE("veri.exe")
timestamp = pe.FILE_HEADER.TimeDateStamp
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp))

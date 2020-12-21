import os
if os.name == 'posix':
    os.system("sudo tcpdump -i en0 -G 900 -s 0 -w ./data/%M_%S.pcap")
else:
    print("not support for windows")


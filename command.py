import os
if os.name == 'posix':
    os.system("sudo tcpdump -X -w ./data/packet.pcap")
else:
    os.system("")


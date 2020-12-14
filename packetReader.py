import pcapy as pc
import struct
import util 
reader = pc.open_offline('./data/packet.pcap')
cnt = 0

while(1):
    (Pkthdr, packet) = reader.next()
    length = len(packet)
    if(length == 0):
        break
    cnt = cnt + 1
    print(cnt)
    rawMac1 = list(struct.unpack('cccccc', packet[0:6]))
    rawMac2 = list(struct.unpack('cccccc', packet[6:12]))
    rawIPType = list(struct.unpack('cc', packet[12:14]))
    hexMac1 = [i.hex() for i in rawMac1]
    hexMac2 = [i.hex() for i in rawMac1]
    IPType = str(rawIPType[0].hex()) + str(rawIPType[1].hex())
    
    mac1 = util.anaMac(rawMac1)
    mac2 = util.anaMac(rawMac2)
    print(mac1)
    print(mac2)
    if(IPType == '0800'):
        IPvertmp = list(struct.unpack('cc', packet[14:16]))
        IPver = int(IPvertmp[0].hex()) // 10
        print(IPver)
    else:
        print('?')



import pcapy as pc
import struct
import IPv4Decode
import EthernetDecode

reader = pc.open_offline('./data/packet.pcap')
cnt = 0

while(1):
    (Pkthdr, packet) = reader.next()
    length = len(packet)
    if(length == 0):
        break
    cnt = cnt + 1
    print(cnt)
    Ethernet = EthernetDecode.Ethernet()
    Ethernet.decodeEthernet(packet[0:14])
    print(Ethernet.srcMac)
    print(Ethernet.dstMac)
    print(Ethernet.IPType)
    if(Ethernet.IPType == '0800'):
        IPv4 = IPv4Decode.IPv4()
        IPv4.decodeIP(packet[14:34])
        print(IPv4.info())
    else:
        print('?')



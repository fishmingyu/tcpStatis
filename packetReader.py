import pcapy as pc
import struct
import util
import TCPDecode
import IPv4Decode
import EthernetDecode
import csv

reader = pc.open_offline('./data/packet2.pcap')
f = open('./data/data.csv','w',encoding='utf-8',newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(util.head())

#while(1):
for i in range(15):
    (Pkthdr, packet) = reader.next()
    length = len(packet)
    if(length == 0):
        break
    Ethernet = EthernetDecode.Ethernet()
    Ethernet.decodeEthernet(packet[0:14])
    
    if(Ethernet.IPType == '0800'): #exclusively decode IPv4
        IPv4 = IPv4Decode.IPv4()
        IPv4.decodeIP(packet[14:34])
        if(IPv4.protocol == 6):
            TCP = TCPDecode.TCP()
            TCP.decodeTCP(packet[34:])
            csvData = Ethernet.data() + IPv4.data() + TCP.data()
            csvWriter.writerow(csvData)


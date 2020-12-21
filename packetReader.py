import pcapy as pc
import struct
import util
import TCPDecode
import UDPDecode
import IPv4Decode
import EthernetDecode
import csv

reader = pc.open_offline('./data/22_02.pcap')
f = open('./data/data.csv','w',encoding='utf-8',newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(util.head())

while(1):
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
        elif(IPv4.protocol == 17):
            UDP = UDPDecode.UDP()
            UDP.decodeUDP(packet[34:42])
            print(UDP.info())
            csvData = Ethernet.data() + IPv4.data() + UDP.data()
            csvWriter.writerow(csvData)
        else:
            csvData = Ethernet.data() + IPv4.data()
            csvWriter.writerow(csvData)


import struct
import socket
from prettytable import PrettyTable
class IPv4(object):
    def __init__(self):
        self.version = None     # 4bit version 
        self.headerlen = None      #4bit header length
        self.tos = None         # 8bit type of service
        self.totalLen = None    # 16bit total length
        self.identification = None  # 16bit header identification
        self.fragment = None        # 16bit others and fragment offset
        self.ttl = None             # 8bit time to live
        self.protocol = None        # 8bit type of protocol
        self.checksum = None    # 16bit header checksum
        self.srcIP = None       # 32bit src IP address
        self.dstIP = None       # 32bit dst IP address
    def decodeIP(self,buffer):
        (versionAndLen,self.tos,self.totalLen,self.identification,self.fragment,
         self.ttl,self.protocol,self.checksum,self.srcIP,self.dstIP) = struct.unpack('>cBHHHBBHII',buffer)
        self.version = str(versionAndLen.hex())[0]
        self.headerlen = str(versionAndLen.hex())[1]
        self.dstIP = socket.inet_ntoa(struct.pack('I',socket.ntohl(self.dstIP)))
        self.srcIP = socket.inet_ntoa(struct.pack('I',socket.ntohl(self.srcIP)))
    def info(self):
        row = PrettyTable()
        row.add_row(['version', self.version])
        row.add_row(['header length', self.headerlen])
        row.add_row(['type of service', self.tos])
        row.add_row(['total length', self.totalLen])
        row.add_row(['header identification', self.identification])
        row.add_row(['others and fragment offset', self.fragment])
        row.add_row(['time to live', self.ttl])
        row.add_row(['type of protocol', self.protocol])
        row.add_row(['header checksum', self.checksum])
        row.add_row(['src IP address', self.srcIP])
        row.add_row(['dst IP address', self.dstIP])
        return row
    def data(self):
        data = []
        data.append(self.version)
        data.append(self.headerlen)
        data.append(self.tos)
        data.append(self.totalLen)
        data.append(self.identification)
        data.append(self.fragment)
        data.append(self.ttl)
        data.append(self.protocol)
        data.append(self.checksum)
        data.append(self.srcIP)
        data.append(self.dstIP)
        return data
        

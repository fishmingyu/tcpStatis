import struct
import socket
from prettytable import PrettyTable
class IPv4(object):
    def __init__(self):
        self.versionAndLen=None   # 4bit version 4bit header length
        self.tos=None             # 8bit type of service
        self.totalLen = None      # 16bit total length
        self.identification =None # 16bit header identification
        self.fragment = None      # 16bit others and fragment offset
        self.ttl = None           # 8bit time to live
        self.protocol = None      # 8bit type of protocol
        self.checksum = None    # 16bit header checksum
        self.srcIP = None       # 32bit src IP address
        self.dstIP = None       # 32bit dst IP address
    def decodeIP(self,buffer):
        (self.versionAndLen,self.tos,self.totalLen,self.identification,self.fragment,
         self.ttl,self.protocal,self.checksum,self.srcIP,self.dstIP) = struct.unpack('>BBHHHBBHII',buffer)
        self.dstIP = socket.inet_ntoa(struct.pack('I',socket.ntohl(self.dstIP)))
        self.srcIP = socket.inet_ntoa(struct.pack('I',socket.ntohl(self.srcIP)))
    def info(self):
        row = PrettyTable()
        row.add_row(['versionAndLen', self.versionAndLen])
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
        


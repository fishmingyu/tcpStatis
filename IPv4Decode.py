import struct
import socket
class IPv4(object):
    def __init__(self):
        self.versionAndLen=None   # 4bit version 4bit header length
        self.tos=None             # 8bit type of service
        self.tolalLen = None      # 16bit total length
        self.identification =None # 16bit header identification
        self.fragment = None      # 16bit others and fragment offset
        self.ttl = None           # 8bit time to live
        self.protocal = None      # 8bit type of protocal
        self.checksum = None    # 16bit header checksum
        self.srcIP = None       # 32bit src IP address
        self.dstIP = None       # 32bit dst IP address
    def decodeIP(self,buffer):
        (self.versionAndLen,self.tos,self.tolalLen,self.identification,self.fragment,
         self.ttl,self.protocal,self.checksum,self.srcIP,self.dstIP) = struct.unpack('>BBHHHBBHII',buffer)
        self.dstIP = socket.inet_ntoa(struct.pack('I',socket.ntohl(self.dstIP)))
        self.srcIP = socket.inet_ntoa(struct.pack('I',socket.ntohl(self.srcIP)))
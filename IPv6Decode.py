import struct
import socket
class IPv6(object):
    def __init__(self):
        self.version=None   # 4bit version
        self.traffic=None             # 8bit trafiic class
        self.flowLabel = None      # 16bit flow label
        self.payload =None # 20bit payload length
        self.nextHeader = None      # 8bit nextHeader
        self.hopLimit = None           # 8bit hop limit
        self.srcIP = None       # 128bit src IP address
        self.dstIP = None       # 128bit dst IP address
        
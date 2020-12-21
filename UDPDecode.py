import struct
from prettytable import PrettyTable

class UDP(object):
    def __init__(self):
        self.srcPort = None     # 16 bit source port
        self.dstPort = None     # 16 bit destination port
        self.length = None         # 16bit length
        self.checksum = None    # 16bit checksum
    def decodeUDP(self,buffer):
        (self.srcPort,self.dstPort,self.length,self.checksum) = struct.unpack('>HHHH',buffer)
    def info(self):
        row = PrettyTable()
        row.add_row(['source port', self.srcPort])
        row.add_row(['destination port', self.dstPort])
        row.add_row(['length', self.length])
        row.add_row(['checksum', self.checksum])
        return row
    def data(self):
        data = []
        data.append(self.srcPort)
        data.append(self.dstPort)
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append('')
        data.append(self.checksum)
        data.append('')
        data.append(self.length)
        return data
        

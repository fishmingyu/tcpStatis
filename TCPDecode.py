import struct
import socket
import util
from bitstring import BitArray
from prettytable import PrettyTable
class TCP(object):
    def __init__(self):
        self.srcPort = None     # source port
        self.dstPort = None      # destination port
        self.seqNum = None         # 32 bit sequece number
        self.ackNum = None    # 32 bit acknowledgement number
        self.dataOffset = None  # 4bit data offset
        self.CWR = None         #congestion window reduced
        self.ECN = None         #ECN-Echo
        self.URG = None             # 1bit URG
        self.ACK = None        # 1bit ACK
        self.PSH = None    # 1bit PSH
        self.RST = None       # 1bit RST
        self.SYN = None       # 1bit SYN
        self.FIN = None         #1bit FIN
        self.winSize = None     #16bit window Size
        self.checksum = None    #16 bit checksum
        self.urgPointer = None  #16bit urgent pointer
        self.payload = None     #?bit payload
    def decodeTCP(self,buffer):
        (self.srcPort,self.dstPort,self.seqNum,self.ackNum,
         offset,control,self.winSize,self.checksum,self.urgPointer) = struct.unpack('>HHIIBcHHH',buffer[0:20])
        self.dataOffset = offset >> 4
        tmp = offset % 16
        tmp = util.bit_to_list(tmp, 4)
        self.Nonce = tmp[3]
        ctlBin = int.from_bytes(control, byteorder='big')
        ctlBin = util.bit_to_list(ctlBin, 8)
        self.CWR = ctlBin[0]
        self.ECN = ctlBin[1]
        self.URG = ctlBin[2]
        self.ACK = ctlBin[3]
        self.PSH = ctlBin[4]
        self.RST = ctlBin[5]
        self.SYN = ctlBin[6]
        self.FIN = ctlBin[7]
        self.payload = len(buffer) - 20
    def info(self):
        row = PrettyTable()
        row.add_row(['source port', self.srcPort])
        row.add_row(['destination port', self.dstPort])
        row.add_row(['sequence number', self.seqNum])
        row.add_row(['acknowledgement number', self.ackNum])
        row.add_row(['data offset', self.dataOffset])
        row.add_row(['Nonce', self.Nonce])
        row.add_row(['CWR', self.CWR])
        row.add_row(['ECN', self.ECN])
        row.add_row(['URG', self.URG])
        row.add_row(['ACK', self.ACK])
        row.add_row(['PSH', self.PSH])
        row.add_row(['RST', self.RST])
        row.add_row(['SYN', self.SYN])
        row.add_row(['FIN', self.FIN])
        row.add_row(['winSize', self.winSize])
        row.add_row(['checksum', self.checksum])
        row.add_row(['urgPointer', self.urgPointer])
        row.add_row(['payload', self.payload])
        return row
    def data(self):
        data = []
        data.append(self.srcPort)
        data.append(self.dstPort)
        data.append(self.seqNum)
        data.append(self.ackNum)
        data.append(self.dataOffset)
        data.append(self.Nonce)
        data.append(self.CWR)
        data.append(self.ECN)
        data.append(self.URG)
        data.append(self.ACK)
        data.append(self.PSH)
        data.append(self.RST)
        data.append(self.SYN)
        data.append(self.FIN)
        data.append(self.winSize)
        data.append(self.checksum)
        data.append(self.urgPointer)
        data.append(self.payload)
        return data
        

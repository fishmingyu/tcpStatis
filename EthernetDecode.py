import struct
from prettytable import PrettyTable
import util
class Ethernet(object):
    def __init__(self):
        self.dstMac=None   # 6bytes destination MAC
        self.srcMac=None   # 6bytes source MAC
        self.IPType = None   # 2bytes IPType

    def decodeEthernet(self,buffer):
        rawMac1 = list(struct.unpack('cccccc', buffer[0:6]))
        rawMac2 = list(struct.unpack('cccccc', buffer[6:12]))
        rawIPType = list(struct.unpack('cc', buffer[12:14]))

        self.dstMac = util.anaMac(rawMac1)
        self.srcMac = util.anaMac(rawMac2)
        self.IPType = rawIPType
        self.IPType = str(rawIPType[0].hex()) + str(rawIPType[1].hex())
    def info(self):
        row = PrettyTable()
        row.add_row(['destination MAC', self.dstMac])
        row.add_row(['source MAC', self.srcMac])
        row.add_row(['IP Type', self.IPType])
        return row
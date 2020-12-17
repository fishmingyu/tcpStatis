def anaMac(rawMac):
    """
    analyze and generate mac address from raw bytes
    """
    for i in rawMac:
        if rawMac.index(i) == 0:
            mac = str(i.hex()) + str(':')
        elif (rawMac.index(i) == len(rawMac) - 1):
            mac = mac + str(i.hex())
        else:
            mac = mac + str(i.hex()) + str(':')
    return mac

def head():
    return ['dstMac', 'srcMac', 'IPType', 'version', 'header length', 'type of service', \
        'total length', 'header identification', 'others and fragment offset', \
        'time to live', 'type of protocol', 'header checksum', 'src IP address', \
        'dst IP address']
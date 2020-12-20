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
        'dst IP address', 'source port', 'destination port', 'sequence number', \
        'acknowledgement number', 'data offset', 'Nonce', 'CWR', 'ECN', 'URG', \
        'ACK', 'PSH', 'RST', 'SYN', 'FIN', 'winSize', 'checksum', 'urgPointer', 'payload']

def bit_to_list(t, n):
    S = [0 for i in range(n)]    
    i = n - 1
    while t != 0:
        S[i] = t % 2
        t = t >> 1
        i -= 1
    return S
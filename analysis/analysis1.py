import os
import csv
import numpy as np
import matplotlib.pyplot as plt


def protocol_type(data, save_path):
    num_TCP_in = 0
    num_TCP_out = 0
    num_UDP_in = 0
    num_UDP_out = 0
    num_other_in = 0
    num_other_out = 0
    group_num_TCP_in = 0
    group_num_TCP_out = 0
    group_num_UDP_in = 0
    group_num_UDP_out = 0
    group_num_other_in = 0
    group_num_other_out = 0
    in_TCP_data = []
    in_UDP_data = []
    out_TCP_data = []
    out_UDP_data = []
    for index in range(len(data)):
        if data[index][1] == 'f0:18:98:50:8d:e9':
            if data[index][10] == '6':
                group_num_TCP_out += 1
                num_TCP_out += int(data[index][6])
                out_TCP_data.append(data[index])
            elif data[index][10] == '17':
                group_num_UDP_out += 1
                num_UDP_out += int(data[index][6])
                out_UDP_data.append(data[index][6])
            else:
                print(f'Upload Unknown Type:{data[index][10]}')
                group_num_other_out += 1
                num_other_out += int(data[index][6])
        elif data[index][0] == 'f0:18:98:50:8d:e9':
            if data[index][10] == '6':
                group_num_TCP_in += 1
                num_TCP_in += int(data[index][6])
                in_TCP_data.append(data[index])
            elif data[index][10] == '17':
                group_num_UDP_in += 1
                num_UDP_in += int(data[index][6])
                in_UDP_data.append(data[index])
            else:
                print(f'Download Unknown Type:{data[index][10]}')
                group_num_other_in += 1
                num_other_in += int(data[index][6])
        else:
            continue
    plt.figure(figsize=(6, 6))
    plt.subplot(2, 2, 1)
    label = ['UDP', 'TCP', 'Other']
    values = [num_UDP_in, num_TCP_in, num_other_in]
    explode = [0.05, 0, 0.05]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Download Message', fontdict={'size': 12})
    plt.subplot(2, 2, 2)
    values = [num_UDP_out, num_TCP_out, num_other_out]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Upload Message', fontdict={'size': 12})
    plt.subplot(2, 2, 3)
    values = [group_num_UDP_in, group_num_TCP_in, group_num_other_in]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Download Groups', fontdict={'size': 12})
    plt.subplot(2, 2, 4)
    values = [group_num_UDP_out, group_num_TCP_out, group_num_other_out]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Upload Groups', fontdict={'size': 12})
    plt.savefig(save_path)

    return in_TCP_data, in_UDP_data, out_TCP_data, out_UDP_data


def port_analysis(data, title, direction):
    port_num = [0] * 65000
    hist = []
    if direction == 'IN':
        for index in range(len(data)):
            hist.append(int(data[index][15]))
            port_num[int(data[index][15])] += 1
    elif direction == 'OUT':
        for index in range(len(data)):
            hist.append(int(data[index][14]))
            port_num[int(data[index][15])] += 1
    plt.hist(hist, bins=20, edgecolor='black')
    plt.yscale("log")
    plt.title(title, fontdict={'size': 9})
    return port_num


def datalen_analysis(data, port_num, title, direction):
    maxten = sorted(port_num, reverse=True)[0:10]
    maxten_port = []
    for i in range(len(maxten)):
        maxten_port.append(port_num.index(maxten[i]))
    maxten_length = []
    if direction == 'IN':
        for index in range(len(data)):
            if int(data[index][15]) in maxten_port:
                maxten_length.append(data[index][6])
    elif direction == 'OUT':
        for index in range(len(data)):
            if int(data[index][14]) in maxten_port:
                maxten_length.append(data[index][6])
    PDF = [0] * (max(maxten_length) + 1)
    CDF = [0] * (max(maxten_length) + 1)
    for i in range(len(maxten_length)):
        PDF[maxten_length[index]] += 1
    CDF[0] = PDF[0]
    for i in range(len(PDF)-1):
        CDF[i + 1] = CDF[i] + PDF[i + 1]
    plt.plot(CDF)
    plt.title(title, fontdict={'size': 9})


if __name__ == '__main__':
    with open('../data/data.csv') as f:
        reader = csv.reader(f)
        data = list(reader)

        '''
        0: dstMac
        1: srcMac
        2: IPType
        3: version
        4: header length
        5: type of service
        6: total length
        7: header identification
        8: others and fragment offset
        9: time to live
        10: type of protocol
        11: header checksum
        12: src IP address
        13: dst IP address
        14: source port
        15: destination port
        16: sequence number
        17: acknowledgement number
        18: data offset
        19: Nonce
        20: CWR
        21: ECN
        22: UGR
        23: ACK
        24: PSH
        25: RST
        26: SYN
        27: FIN
        28: winSize
        29: checksum
        30: urgPointer
        31: payload
        '''

        in_TCP_data, in_UDP_data, out_TCP_data, out_UDP_data = protocol_type(data, '../img/Protocol_Type.jpg')
        plt.figure(figsize=(6, 6))
        plt.subplot(2, 2, 1)
        port_num_1 = port_analysis(in_TCP_data, 'Download TCP Distribution', direction='IN')
        plt.subplot(2, 2, 2)
        port_num_2 = port_analysis(out_TCP_data, 'Upload TCP Distribution', direction='OUT')
        plt.subplot(2, 2, 3)
        port_num_3 = port_analysis(in_UDP_data, 'Download UDP Distribution', direction='IN')
        plt.subplot(2, 2, 4)
        port_num_4 = port_analysis(out_UDP_data, 'Upload UDP Distribution', direction='OUT')
        plt.savefig('../img/all.jpg')
        plt.figure(figsize=(6, 6))
        plt.subplot(2, 2, 1)
        datalen_analysis(data, port_num_1, 'Download TCP message length distribution', direction='IN')
        plt.subplot(2, 2, 2)
        datalen_analysis(data, port_num_2, 'Upload TCP message length distribution', direction='OUT')
        plt.subplot(2, 2, 3)
        datalen_analysis(data, port_num_3, 'Download UDP message length distribution', direction='IN')
        plt.subplot(2, 2, 4)
        datalen_analysis(data, port_num_4, 'Upload UDP message length distribution', direction='OUT')
        plt.savefig('../img/CDF.jpg')

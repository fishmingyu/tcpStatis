import os
import csv
import matplotlib.pyplot as plt


def protocol_type(data, save_path):
    out_TCP_data = []
    out_UDP_data = []
    in_TCP_data = []
    in_UDP_data = []
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
    for index in range(len(data)):
        if data[index][1] == 'f0:18:98:50:8d:e9':
            if data[index][10] == '6':
                group_num_TCP_out += 1
                num_TCP_out += int(data[index][6]) - int(data[index][4])
                out_TCP_data.append(data[index])
            elif data[index][10] == '17':
                group_num_UDP_out += 1
                num_UDP_out += int(data[index][6]) - int(data[index][4])
                out_UDP_data.append(data[index])
            else:
                print(f'Upload Unknown Type:{data[index][10]}')
                group_num_other_out += 1
                num_other_out += int(data[index][6]) - int(data[index][4])
        elif data[index][0] == 'f0:18:98:50:8d:e9':
            if data[index][10] == '6':
                group_num_TCP_in += 1
                num_TCP_in += int(data[index][6]) - int(data[index][4])
                in_TCP_data.append(data[index])
            elif data[index][10] == '17':
                group_num_UDP_in += 1
                num_UDP_in += int(data[index][6]) - int(data[index][4])
                in_UDP_data.append(data[index])
            else:
                print(f'Download Unknown Type:{data[index][10]}')
                group_num_other_in += 1
                num_other_in += int(data[index][6]) - int(data[index][4])
        else:
            continue
    plt.figure(figsize=(6, 6))
    label = ['UDP', 'TCP']
    explode = [0.05, 0]

    values = [num_UDP_in, num_TCP_in]
    plt.subplot(2, 2, 1)
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Download Data')
    plt.subplot(2, 2, 2)
    values = [num_UDP_out, num_TCP_out]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Upload Data')
    plt.subplot(2, 2, 3)
    values = [group_num_UDP_in, group_num_TCP_in]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Download Packets')
    plt.subplot(2, 2, 4)
    values = [group_num_UDP_out, group_num_TCP_out]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Total Upload Group')
    plt.savefig(save_path)

    return out_TCP_data, out_UDP_data, in_TCP_data, in_UDP_data


def port_analysis(data, direction, title):
    port_num = [0] * 70000  # port_num数组下标为端口号，值为相应端口的消息数量
    hist = []  # hist为所有消息的端口号的无序重复排列
    if direction == 'IN':  # 入出方向的判别方法与第1小题相同
        for index in range(len(data)):
            hist.append(int(data[index][15]))
            port_num[int(data[index][15])] += 1
    elif direction == 'OUT':
        for index in range(len(data)):
            hist.append(int(data[index][14]))
            port_num[int(data[index][14])] += 1
    plt.hist(hist, bins=20, log=True, edgecolor='black')
    plt.title(title)
    max_port = [int(port_num.index(i)) for i in sorted(port_num, reverse=True)[0:10]]
    return max_port


def datalen_analysis(data, max_ports, direction, save_path):
    plt.figure(figsize=(12, 18))
    for i, max_port in enumerate(max_ports):
        maxten_length = []
        if direction == 'IN':
            for index in range(len(data)):
                if int(data[index][15]) == max_port:
                    maxten_length.append(int(data[index][6]))
        elif direction == 'OUT':
            for index in range(len(data)):
                if int(data[index][14]) == max_port:
                    maxten_length.append(int(data[index][6]))
        PDF = [0] * (max(maxten_length) + 1)
        CDF = [0] * (max(maxten_length) + 1)
        for index in range(len(maxten_length)):
            PDF[maxten_length[index]] += 1
        CDF[0] = PDF[0]
        for index in range(len(PDF)-1):
            CDF[index + 1] = CDF[index] + PDF[index + 1]
        plt.subplot(5, 2, i + 1)
        plt.plot(CDF)
        plt.ylabel('packet number')
        plt.title(f'port: {max_port}')
    plt.savefig(save_path)


if __name__ == '__main__':
    with open('./data/data.csv') as f:
        reader = csv.reader(f)
        data = list(reader)

        out_TCP_data, out_UDP_data, in_TCP_data, in_UDP_data = protocol_type(data, './img/protocol_type.jpg')

        plt.figure(figsize=(6, 6))
        plt.subplot(2, 2, 1)
        max_port_1 = port_analysis(in_TCP_data, 'IN', 'Download TCP Distribution')
        plt.subplot(2, 2, 2)
        max_port_2 = port_analysis(out_TCP_data, 'OUT', 'Upload TCP Distribution')
        plt.subplot(2, 2, 3)
        max_port_3 = port_analysis(in_UDP_data, 'IN', 'Download UDP Distribution')
        plt.subplot(2, 2, 4)
        max_port_4 = port_analysis(out_UDP_data, 'OUT', 'Upload UDP Distribution')
        plt.savefig('./img/all.jpg')

        datalen_analysis(in_TCP_data, max_port_1, 'IN', './img/Download_TCP_CDP.jpg')
        datalen_analysis(out_TCP_data, max_port_2, 'OUT', './img/Upload_TCP_CDP.jpg')
        datalen_analysis(in_UDP_data, max_port_3, 'IN', './img/Download_UDP_CDP.jpg')
        datalen_analysis(out_UDP_data, max_port_4, 'OUT', './img/Upload_UDP_CDP.jpg')

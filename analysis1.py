import os
import csv
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
    for index in range(len(data)):
        if data[index][12] == '172.30.3.167':
            if data[index][10] == '6':
                group_num_TCP_out += 1
                num_TCP_out += int(data[index][6])
            elif data[index][10] == '17':
                group_num_UDP_out += 1
                num_UDP_out += int(data[index][6])
            else:
                print(f'Upload Unknown Type:{data[index][10]}')
                group_num_other_out += 1
                num_other_out += int(data[index][6])
        elif data[index][13] == '172.30.3.167':
            if data[index][10] == '6':
                group_num_TCP_in += 1
                num_TCP_in += int(data[index][6])
            elif data[index][10] == '17':
                group_num_UDP_in += 1
                num_UDP_in += int(data[index][6])
            else:
                print(f'Download Unknown Type:{data[index][10]}')
                group_num_other_in += 1
                num_other_in += int(data[index][6])
        else:
            continue
    plt.figure(figsize=(6, 6))
    label = ['UDP', 'TCP', 'Other']
    values = [num_UDP_in, num_TCP_in, num_other_in]
    explode = [0.05, 0, 0.05]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Total Download Data')
    plt.savefig(os.path.join(save_path, 'DownloadData.jpg'))

    plt.figure(figsize=(6, 6))
    values = [num_UDP_out, num_TCP_out, num_other_out]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Total Upload Data')
    plt.savefig(os.path.join(save_path, 'UploadData.jpg'))

    plt.figure(figsize=(6, 6))
    values = [group_num_UDP_in, group_num_TCP_in, group_num_other_in]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Total Download Group')
    plt.savefig(os.path.join(save_path, 'DownloadGroup.jpg'))

    plt.figure(figsize=(6, 6))
    values = [group_num_UDP_out, group_num_TCP_out, group_num_other_out]
    plt.pie(values, explode, label, autopct='%3.2f%%')
    plt.title('Total Upload Group')
    plt.savefig(os.path.join(save_path, 'UploadGroup.jpg'))


if __name__ == '__main__':
    with open('./data/data.csv') as f:
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
        '''

        protocol_type(data, './plt')
        print(data[1])
        print(data[2])
        print(data[3])

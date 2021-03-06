# get inputs

def max_init(car_list2):
    car_dic = {}
    car_list = []
    maximum = 0
    for car in car_list2:
        if car[0] >= maximum:
            maximum = car[0]

        car_list.append(car[1:])

    for index in range(maximum):
        temp = {}
        for car in car_list:
            if len(car) - 1 >= index:
                if car[index] not in temp.keys():
                    temp[car[index]] = 0
                temp[car[index]] += 1
        for key in temp.keys():
            if key not in car_dic:
                car_dic[key] = []
            car_dic[key].append(temp[key])

    for each_1 in car_dic.keys():
        car_dic[each_1] = max(car_dic[each_1])
    return car_dic


def max_thari(path_list, street, I):
    for intersection in range(I):
        ap_streets = []
        for road in street:
            if (road[1] == intersection):
                ap_streets.append(road[2])

    # for each in street:
    #    name = each[2]


def output(dic):
    st = ""
    st += str(I) + '\n'
    for i in range(I):
        st += str(i) + '\n'
        st += str(inter_cnt[i]) + '\n'
        for j in path_inter[i]:
            st += f'{reverse_enc[j]} {dic[j]}\n'
    return st


if __name__ == "__main__":
    root = 'D:/Hashcode/2021/qulification round/'
    file_path = 'b.txt'
    list_data_lines = []
    name_enc = {}
    inter_cnt = {}
    path_inter = {}
    desc_street = []
    desc_path = []
    with open(root + file_path, 'r') as pf:
        for line in pf.readlines():
            fil_line = line.strip('\n').split()
            list_data_lines.append(fil_line)
    n = 0
    for i in range(len(list_data_lines)):
        if i == 0:
            D, I, S, V, F = [int(j) for j in list_data_lines[i]]
        elif i < S + 1:
            B, E, name, L = list_data_lines[i]
            E = int(E)
            try:
                enc = name_enc[name]
            except:
                enc = n
                n += 1
                name_enc[name] = enc

            try:
                inter_cnt[E] += 1
                path_inter[E].append(enc)
            except:
                inter_cnt[E] = 1
                path_inter[E] = [enc]

            desc_street.append([int(B), int(E), enc, int(L)])
        else:
            P, *names = list_data_lines[i]
            enc_list = []
            for k in names:
                try:
                    enc = name_enc[k]
                except:
                    enc = n
                    n += 1
                    name_enc[k] = enc
                enc_list.append(enc)
            desc_path.append([int(P), ] + enc_list)
    reverse_enc = dict(zip(name_enc.values(), name_enc.keys()))

    max_dict = max_init(desc_path)

    with open(root + 'test2.txt', 'w') as pf:
        pf.write(output(max_dict))

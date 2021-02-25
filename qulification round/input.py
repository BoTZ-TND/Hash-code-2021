# get inputs

def max_init(car_list):
    car_dic = {}
    maximum = 0
    for car in car_list:
        if len(car) >= maximum:
            maximum = len(car)

    for index in range(maximum):
        print(index)
        temp = {}
        for car in car_list:
            if len(car)-1>= index:
                if car[index] not in temp.keys():
                    temp[car[index]] = 0
                temp[car[index]] += 1
        for key in temp.keys():
            if key not in car_dic:
                car_dic[key] = []
            car_dic[key].append(temp[key])

    print(car_dic)
    for each_1 in car_dic.keys():
        car_dic[each_1] = max(car_dic[each_1])
    print(car_dic)
    return car_dic


if __name__ == "__main__":
    root = 'D:/Hashcode/2021/qulification round/'
    file_path = 'a.txt'
    list_data_lines = []
    name_enc = {}
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
            try:
                enc = name_enc[name]
            except:
                enc = n
                n += 1
                name_enc[name] = enc
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
    print(desc_path)
    print(desc_street)
    print(name_enc)
    print(reverse_enc)

    max_init(desc_path)

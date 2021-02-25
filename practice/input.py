# get inputs

ing_dict = {}


def name_encoder(ing_arr):
    i = 0
    enc_lis = []
    for arr in ing_arr:
        ing_sts = arr[1:]
        return_lis = [int(arr[0]), ]
        for ing in ing_sts:
            try:
                return_lis.append(ing_dict[ing])
            except:
                ing_dict[ing] = i
                i += 1
                return_lis.append(i)
        enc_lis.append(return_lis)
    return enc_lis


def index_list(num_list):
    dic = {}
    for index in range(len(num_list)):
        if num_list[index] not in dic:
            dic[num_list[index]] = []

        dic[num_list[index]].append(index)

    return dic


def combinations(num_list):
    dic = {}
    for first in range(len(num_list)):
        for second in range(first+1, len(num_list)):
            if num_list[first] + num_list[second] not in dic:
                dic[num_list[first] + num_list[second]] = []
            dic[num_list[first] + num_list[second]].append([first, second])

    return dic


if __name__ == '__main__':
    # file_name =
    root = 'D:/Hashcode/2021'
    data_list = []
    with open(root + "/practice/data/b_little_bit_of_everything.txt", "r") as pf:
        for line in pf.readlines():
            line_lis = line.rstrip('\n').split(' ')
            data_list.append(line_lis)
    teams = [int(i) for i in data_list[0]]
    ing_list = name_encoder(data_list[1:])
    print(ing_list)
    for each in ing_list:
        print(each[0])
        print(index_list(each[1:]))
        print(combinations(each[1:]))


# get inputs

ing_dict = {}

def name_encoder(ing_arr):
    i = 0
    enc_lis = []
    for arr in ing_arr:
        ing_sts = arr[1:]
        return_lis = [int(arr[0]),]
        for ing in ing_sts:
            try:
                return_lis.append(ing_dict[ing])
            except:
                ing_dict[ing] = i
                i += 1
                return_lis.append(i)
        enc_lis.append(return_lis)
    return enc_lis

if __name__ == '__main__':
    #file_name = 
    root = 'F:/JetBrain Project Files/Pycharm'
    data_list = []
    with open(root+"/Hash-code-2021/practice/data/b_little_bit_of_everything.txt","r") as pf:
        for line in pf.readlines():
            line_lis = line.rstrip('\n').split(' ')
            data_list.append(line_lis)
    teams = [int(i) for i in data_list[0]]
    ing_list = name_encoder(data_list[1:])
    print(ing_list)

# get inputs

if __name__ == "__main__":
    root = 'F:/JetBrain Project Files/Pycharm/Hash-code-2021/qulification round/'
    file_path = 'a.txt'
    list_data_lines = []
    name_enc = {}
    inter_cnt = {}
    path_inter = {}
    desc_street = []
    desc_path = []
    with open(root+file_path, 'r') as pf:
        for line in pf.readlines():
            fil_line = line.strip('\n').split()
            list_data_lines.append(fil_line)
    n = 0
    for i in range(len(list_data_lines)):
        if i == 0:
            D, I, S, V, F = [int(j) for j in list_data_lines[i]]
        elif i < S+1:
            B, E, name, L = list_data_lines[i]

            try:
                enc = name_enc[name]
            except:
                enc = n
                n +=1
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
            desc_path.append([int(P),]+enc_list)

    print(desc_path)
    print(desc_street)
    print(name_enc)

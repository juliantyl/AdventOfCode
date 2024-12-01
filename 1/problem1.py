
if __name__ == '__main__':
    ls1 = []
    ls2 = []
    with open('input1.txt', 'r') as file:
        for line in file:
            line_f = line.strip().split(" ")
            ls1.append(int((line_f[0])))
            ls2.append(int(line_f[3]))
    sorted_ls1 = sorted(ls1)
    sorted_ls2 = sorted(ls2)

    dist = 0
    for i in range(len(sorted_ls1)):
        dist += abs(sorted_ls1[i] - sorted_ls2[i])
    print(dist)

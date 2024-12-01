
if __name__ == '__main__':
    ls1 = []
    ls2 = []
    with open('input1.txt', 'r') as file:
        for line in file:
            line_f = line.strip().split(" ")
            ls1.append(int((line_f[0])))
            ls2.append(int(line_f[3]))
    dict1 = {}
    dict2 = {}
    for item in ls1:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    for item in ls2:
        if item in dict2:
            dict2[item] += 1
        else:
            dict2[item] = 1

    output = 0
    for i in ls1:
        if i not in dict2:
            continue
        else:
            output += i * dict2[i]
    print(output)

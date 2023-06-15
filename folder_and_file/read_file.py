path = 'target.txt'
f = open(path, 'r')
for line in f.readlines():
    print(line)
    splitValue = line.split(",")
    for single in splitValue:
        print(single)
    print("end split")
f.close()

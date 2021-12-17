def Autotest_1():
    test = open("Autotest.txt", "w+")
    test.write("1 1 3")
    test.close()
    func("AutoTest.txt")
    if func("AutoTest.txt") == 2:
        return 1
    return 0


def Autotest_2():
    test = open("Autotest.txt", "w+")
    test.write("1 0 1 0 3")
    test.close()
    func("AutoTest.txt")
    if func("AutoTest.txt") == 2:
        return 1
    return 0

def Autotest_3():
    test = open("Autotest.txt", "w+")
    test.write("1 -2 1 0 3")
    test.close()
    func("AutoTest.txt")
    if func("AutoTest.txt") == 1:
        return 1
    return 0


def autotest():
    if Autotest_1() == 1:
        print("First autotest passed")
    else:
        print("First autotest failed")
    if Autotest_2() == 1:
        print("Second autotest passed")
    else:
        print("Second autotest failed")
    if Autotest_3() == 1:
        print("Third autotest passed\n")
    else:
        print("Third autotest failed\n")


def func(name_of_file):
    a = 0
    k = False
    file = open(name_of_file, "r")
    if file.closed:
        print('file is closed')
        return 0
    for line in file:
        seq = line.split()
        for i in range(1, len(seq) - 1):
            if seq[i].isdigit:
                if seq[i] <= seq[i-1]:
                    if seq[i] < seq[i+1]:
                     if k:
                            if seq[i] != a:
                             return 1
                     else:
                         a = seq[i]
                         k = True
        if seq[0] < seq [1]:
            if k:
                if seq[0] != a:
                    return 1
            else:
                a = seq[i]
        if seq[len(seq) - 1] < seq [len(seq) - 2]:
            if k:
                if seq[len(seq) - 1] != a:
                    return 1
            else:
                a = seq[i]
    return 2
    file.close()

autotest()
print("Write name of file:")
f = input()
if func(f) == 2:
    print('All local minimums are equal \n')
else:
    print('All local minimums are not equal \n')

#  passed

import sys
import math

def read_str():
    return input()

def read_strs():
    return list(input().split())

def read_ints():
    return list(map(int, input().split()))

def read_int():
    return int(input())


def solve(case_no):
    n=read_int()
    given=read_str()
    gec = 0
    gsc = 0
    gcordinates = [[0, 0]]
    for x in given:
        if (x == "E"):
            gec += 1
            gcordinates.append([gsc, gec])
        elif (x == "S"):
            gsc += 1
            gcordinates.append([gsc, gec])
    # [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [4, 3], [4, 4]]
    step = 0

    px = 0
    py = 0

    pcordinates = [[0, 0]]
    trappeddif = [-1, -1]
    diff = []
    tcord = [0, 0]

    while (pcordinates[len(pcordinates) - 1] != [n - 1, n - 1]):
        tokentrapped = 0
        diff = [x - y for x, y in zip(gcordinates[step + 1], gcordinates[step])]
        if (diff == [0, 1]):
            if (py <= n - 1 and (trappeddif == [0, 1] or trappeddif == [-1, -1])):
                py += 1
                step += 1
            else:
                tcord = [px, py]
                py -= 1
                trappeddif = [x - y for x, y in zip(tcord, [px, py])]
                tokentrapped = 1

        elif (diff == [1, 0]):
            if (px <= n - 1 and (trappeddif == [0, 1] or trappeddif == [-1, -1])):
                px += 1
                step += 1
            else:
                tcord = [px, py]
                px -= 1
                trappeddif = [x - y for x, y in zip(tcord, [px, py])]
                tokentrapped = 1

        if (tokentrapped == 0):
            pcordinates.append([px, py])
        else:
            del pcordinates[-1]

    str = ''
    for i in range(0, len(pcordinates) - 1):
        if ([x - y for x, y in zip(pcordinates[i + 1], pcordinates[i])] == [0, 1]):
            str += 'S'
        elif ([x - y for x, y in zip(pcordinates[i + 1], pcordinates[i])] == [1, 0]):
            str += 'E'
    print('Case #%d: %s' % (case_no, str))

def main():
    T, = read_ints()
    for t in range(T):
        solve(t+1)


if __name__ == '__main__':
    main()

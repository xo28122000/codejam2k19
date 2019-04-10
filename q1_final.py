#  passed

import sys
import math

def read_str():
    return input()

def read_strs():
    return list(input().split())

def read_ints():
    return list(map(int, input().split()))

def solve(case_no):

    n, = read_ints()

    i = 0
    while (i < n / 2):
        j = n - i


        n1 = list(map(int, str(i)))
        n2 = list(map(int, str(j)))
        t1 = 1
        t2 = 1
        repi = -1
        repj = -1

        for m in reversed(n1):
            if (m == 4):
                t1 = 0
                repi += 1

                break
            else:
                repi += 1
        else:
            repi = 0

        for m in reversed(n2):
            if (m == 4):
                t2 = 0
                repj += 1
                break
            else:
                repj += 1
        else:
            repj = 0



        if (t1 == 1 and t2 == 1):
            print('Case #%d: %s %s' % (case_no,i,j))
            break
        elif (t2 == 0 and t1 == 1):
            i += pow(10, repj)
        elif (t1 == 0 and t2 == 1):
            i += pow(10, repi)
        else:
            if (repj > repi):
                i += pow(10, repj)
            else:
                i += pow(10, repi)






def main():
    T, = read_ints()
    for t in range(T):
        solve(t+1)


if __name__ == '__main__':
    main()


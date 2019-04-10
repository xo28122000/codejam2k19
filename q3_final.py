#  failed


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
    line1con=read_str()
    wordlist=read_ints()

    result = []
    res = []

    for word in wordlist:
        temp = []
        i = 2

        while i * i <= word:
            if word % i == 0:
                temp.append(i)

                if word / i != i:
                    temp.append(int(word / i))
            i += 1
        res.append(temp)
        for x in temp:
            if x not in result:
                result.append(int(x))

    result.sort()
    cyperdict = {}
    alpha = 'A'
    for x in result:
        cyperdict[x] = alpha
        alpha = chr(ord(alpha) + 1)
    fstring = ''
    j = 0
    while (j < len(res)):
        if (j == len(res) - 1):
            for x in res[j]:
                if (x in res[j - 1]):
                    fstring += cyperdict[x]
                elif (x not in res[j - 1]):
                    fstring += cyperdict[x]
        else:
            for x in res[j]:
                if (x not in res[j + 1]):
                    fstring += cyperdict[x]
        j += 1

    print('Case #%d: %s' % (case_no, fstring))


def main():
    T, = read_ints()
    for t in range(T):
        solve(t+1)


if __name__ == '__main__':
    main()
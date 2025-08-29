import sys


def main():
    s = input()
    d = {}
    l = len(s)
    for i in range(l):
        if s[i] in d:
            d[s[i]] += (i + 1) * (l - i)
        else:
            d[s[i]] = (i + 1) * (l - i)
    for i in range(97, 123):
        if chr(i) in d:
            print(chr(i) + ": " + str(d[chr(i)]))



if __name__ == '__main__':
    main()
import sys


def main():
    d = {}
    for line in sys.stdin:
        line = str.strip(line)
        if line == '':
            break
        s = list(map(str, line.split()))
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

    d = sorted(d.items(), reverse=True)
    d = sorted(d, key=lambda x: x[1])
    print(d[-1][0])


if __name__ == '__main__':
    main()

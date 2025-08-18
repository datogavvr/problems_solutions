import sys


def main():
    x, y = map(int, input().split(' / '))
    n = int(input())
    req = list(map(int, input().split()))
    ans = []
    if x == 1:
        y *= 10 ** 9
        ans.append(req[0])
        for i in range(1, len(req)):
            ans.append(max(ans[i - 1] + y, req[i]))
    else:
        sec = list(req[i] for i in range(x))
        for i in range(x):
            ans.append(req[i])

        val_in_sec = len(sec)
        for i in req[x:]:
            while i >= sec[0] + 10 ** 9:
                del sec[0]
                val_in_sec -= 1
                if val_in_sec == 0:
                    break
            if val_in_sec < x:
                sec.append(i)
                ans.append(i)
                val_in_sec += 1
            else:
                sec.append(sec[0] + 10 ** 9)
                ans.append(sec[0] + 10 ** 9)
                del sec[0]
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
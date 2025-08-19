import sys


def main():
    n = int(input())
    l = 0 # длина очереди
    queue = [] # куеуе
    for i in range(n):
        goblin = list(map(str, input().split()))
        if goblin[0] == '+':
            queue.append(goblin[1])
            l += 1
        elif goblin[0] == '*':
            if l % 2 == 0:
                queue.insert(l//2, goblin[1])
            else:
                queue.insert(l//2 + 1, goblin[1])
            l += 1
        else:
            print(queue.pop(0))
            l -= 1



if __name__ == '__main__':
    main()

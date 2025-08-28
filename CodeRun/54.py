import sys


def main():
    at_least_one = set()
    students = []
    n = int(input())
    for i in range(n):
        m = int(input())
        students.append([])
        for j in range(m):
            language = input()
            students[i].append(language)
            at_least_one.add(language)
    every_one = set([i for i in students[0]])
    for i in range(1, n):
        every_one = every_one & set(students[i])
    print(len(every_one))
    for i in every_one:
        print(i)
    print(len(at_least_one))
    for i in at_least_one:
        print(i)


if __name__ == '__main__':
    main()

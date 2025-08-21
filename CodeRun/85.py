import sys


def main():
    buyers = {}

    for line in sys.stdin:
        if line.strip() == (''):
            break
        buyer, product, count = map(str, line.strip().split())
        count = int(count)
        if buyer in buyers:
            if product in buyers[buyer]:
                buyers[buyer][product] += count
            else:
                buyers[buyer][product] = count
        else:
            buyers[buyer] = {product: count}

    buyers = dict(sorted(buyers.items()))
    for i in buyers:
        buyers[i] = dict(sorted(buyers[i].items()))

    for i in buyers:
        print(i + ':')
        for j in buyers[i]:
            print(j + ' ' + str(buyers[i][j]))


if __name__ == '__main__':
    main()
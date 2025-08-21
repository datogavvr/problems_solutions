a = {'ivanov': [['moloko', 1], ['aboba', 3], ['labuba', 2]], 'anreev': [['skibidi', 5]]}
a = dict(sorted(a.items()))
for i in a:
    a[i].sort()
if 9 in a:
    print(1)
else:
    print(0)
print(a)
d = dict()
for i in range(int(input())):
    a = input().split()
    if a[2] not in d:
        d[a[2]] = int(a[3])
    else:
        d[a[2]] = (int(d[a[2]]) + int(a[3])) / 2
d = list(filter(lambda x: d[x] == max(d.values()), d))
print(*d)
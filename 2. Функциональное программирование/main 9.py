import itertools

N, K = map(int, input().split())

print(list(itertools.combinations(str(N), K)))
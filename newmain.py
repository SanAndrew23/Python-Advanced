from itertools import permutations
# Большой квадрат
print('1.1:')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
max_cover = 0
an = max(min(a, b), min(c, d))

oper = [ #Варианты расположения
    ((a, b), (c, d)),
    ((a, b), (d, c)),
    ((b, a), (c, d)),
    ((b, a), (d, c))
]
for (x1, y1), (x2, y2) in oper:
    side1 = min(x1 + x2, min(y1, y2))
    side2 = min(min(x1, x2), y1 + y2)
    an = max(an, side1, side2)
print(an)
'''
#2 План эвакуации
n = int(input())
m = int(input())
matrix = [[0 for i in range(m)] for j in range(n)]

x1 = int(input()) - 1
y1 = int(input()) - 1
matrix[x1][y1] = 'S'


x2 = int(input()) - 1
y2 = int(input()) - 1
matrix[x2][y2] = 'S'

#заполнение вокруг лестниц
if y1 - 1 >= 0:
    matrix[x1][y1 - 1] = '>'
if y2 - 1 >= 0:
    matrix[x2][y2 - 1] = '>'
if y1 + 1 <= n:
    matrix[x1][y1 + 1] = '<'
if y2 + 1 <= m:
    matrix[x2][y2 + 1] = '<'
if x1 - 1 >= 0:
    matrix[x1 - 1][y1] = 'ВН'
if x2 - 1 >= 0:
    matrix[x2 - 1][y2] = 'ВН'
if x1 + 1 <= n:
    matrix[x1 + 1][y1] = 'ВВ'
if x2 + 1 <= n:
    matrix[x2 + 1][y2] = 'ВВ'
print(matrix)'''
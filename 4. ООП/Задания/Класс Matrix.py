from pkgutil import resolve_name


class Matrix:
    def __init__(self, rows=0, cols=0, *, data=None):
        if data is None:
            self.rows = rows
            self.cols = cols
            self.matrix = [[0 for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.matrix = data
            self.rows = len(data)
            self.cols = len(data[0])

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = [[0 for j in range(self.cols)] for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(data=result)
        else:
            raise ValueError('Размеры матриц не совпадают.')

    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = [[0 for j in range(self.cols)] for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return Matrix(data=result)
        else:
            raise ValueError('Размеры матриц не совпадают.')

    def __mul__(self, other):
        result = [[0 for j in range(self.cols)] for i in range(self.rows)]
        if isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] = self.matrix[i][j] * other
            return Matrix(data=result)
        elif self.cols == other.rows:
            result = [[0 for j in range(other.cols)] for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(data=result)
        else:
            raise ValueError('Размеры матриц не совпадают.')

    def transpose(self):
        result = [[0 for j in range(self.rows)] for i in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = matrix1[i][j]
        return Matrix(data=result)

    def __str__(self):
        lines = []
        m_s = len(str(max(x for row in self.matrix for x in row)))
        for row in self.matrix:
            row_s = ''.join(f'{i : {m_s + 1}}' for i in row)
            lines.append(row_s)
        return '\n'.join(lines)


matrix1 = Matrix(data=[[1, 2], [4, 5]])
matrix2 = Matrix(data=[[7, 8], [10, 11]])
try:
    print(matrix1 + matrix2)
    print()
    print(matrix1 - matrix2)
    print()
    print(matrix1 * matrix2)
    print()
    print(matrix1.transpose())
except ValueError:
    print(f'Ошибка: размеры матриц не совпадают')

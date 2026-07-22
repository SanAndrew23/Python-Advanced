class Matrix:
    def __init__(self, rows=None, cols=None):
        if isinstance(rows, int):
            self.rows = rows
            self.cols = cols
            self.matrix = [[0 for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.matrix = rows
            self.cols = len(rows[0])
            self.rows = len(rows)
    def __getitem__(self, index):
        return self.matrix[index]
    def __add__(self, other):

    def __sub__(self, other):

    def __mul__(self, other):

    def transpose(self):

    def __str__(self):
        s = ''
        for i in range(0, self.rows - 1):
            for j in range(0, self.cols - 1):
                s += str(self.matrix[i][j]) + ' '
        return s


matrix = Matrix(5, 2)
print(matrix)

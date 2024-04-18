# Defining the classes and functions needed for priority queue, sparse matrix and lower triangular matrix

class PriorityQueue:
    def __init__(self):
        self.queue = []
   
    def insert(self, data, priority):
        # Insert element according to its priority
        self.queue.append((data, priority))
        self.queue.sort(key=lambda x: x[1], reverse=True)
   
    def extract(self):
        # Extract the element with the highest priority
        if self.is_empty():
            raise IndexError("Extract from an empty priority queue")
        return self.queue.pop(0)
   
    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return ' '.join([str(i[0]) for i in self.queue])


class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = {}
   
    def insert(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
   
    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.elements.get((row, col), 0), end=' ')
            print()


class LowerTriangularMatrix:
    def __init__(self, size):
        self.size = size
        self.elements = [0] * (size * (size + 1) // 2)
   
    def insert(self, row, col, value):
        if row >= col:
            index = self.size * col - col * (col - 1) // 2 + row - col
            self.elements[index] = value
   
    def display(self):
        for row in range(self.size):
            for col in range(self.size):
                if row >= col:
                    index = self.size * col - col * (col - 1) // 2 + row - col
                    print(self.elements[index], end=' ')
                else:
                    print(0, end=' ')
            print()

# Next, I will write the logic to read a matrix from a CSV file and check if it is sparse
# The filepath provided will be used to locate the CSV file and read it into the program

import csv

def read_matrix_from_csv(filepath):
    matrix = []
    with open(filepath, newline='') as csvfile:
        matrix_reader = csv.reader(csvfile, delimiter=',')
        for row in matrix_reader:
            matrix.append([int(x) if x else 0 for x in row])
    return matrix

def is_sparse_matrix(matrix):
    non_zero_count = sum(x != 0 for row in matrix for x in row)
    total_elements = len(matrix) * len(matrix[0])
    return non_zero_count / total_elements < 0.1

# Function to create a sparse matrix representation if the matrix is sparse

def create_sparse_matrix_representation(matrix):
    rows, cols = len(matrix), len(matrix[0])
    sparse_matrix = SparseMatrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse_matrix.insert(i, j, matrix[i][j])
    return sparse_matrix

# Let's comment out the following function calls to prevent execution during development
# filepath = "C:\\Users\\p.horvath\\OneDrive - BFI Burgenland\\Desktop\\mock_matrix.csv"
# matrix = read_matrix_from_csv(filepath)
# if is_sparse_matrix(matrix):
#     sparse_matrix = create_sparse_matrix_representation(matrix)
#     sparse_matrix.display()
# Updating the CSV reading function to handle semicolon (;) as delimiter
def read_matrix_from_csv_semicolon(filepath):
    matrix = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        matrix_reader = csv.reader(csvfile, delimiter=';')
        for row in matrix_reader:
            matrix.append([int(x) if x else 0 for x in row if x.strip()])
    return matrix

# Uncommenting the file path and reading logic with the new delimiter and checking if the matrix is sparse
# Also, ensuring the matrix elements are processed correctly by stripping whitespace

# Function to read and process a matrix from the updated CSV file
# filepath = "C:\\Users\\p.horvath\\OneDrive - BFI Burgenland\\Desktop\\mock_matrix.csv"
# matrix = read_matrix_from_csv_semicolon(filepath)
# if is_sparse_matrix(matrix):
#     sparse_matrix = create_sparse_matrix_representation(matrix)
#     sparse_matrix.display()

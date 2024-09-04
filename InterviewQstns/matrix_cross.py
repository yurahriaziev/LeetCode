def solution(matrix):
    if len(matrix) == 0:
        return None
    
    rows = len(matrix)
    cols = len(matrix[0])
    crosses = 0

    sols = []

    for i in range(rows):
        for j in range(cols):
            nbors = []
            sol = [[0 for i in range(cols)] for j in range(rows)]
            for k in range(1, max(len(matrix), len(matrix[i]))):
                if i - k >= 0:
                    nbors.append(matrix[i-k][j])
                    sol[i-k][j] = '|'
                if j + k < len(matrix[i]):
                    nbors.append(matrix[i][j+k])
                    sol[i][j+k] = '-'
                if i + k < len(matrix):
                    nbors.append(matrix[i+k][j])
                    sol[i+k][j] = '|'
                if j - k >= 0:
                    nbors.append(matrix[i][j-k])
                    sol[i][j-k] = '-'
            cross = True
            for num in range(len(nbors)-1):
                if nbors[num] != nbors[num+1]:
                    cross = False

            if cross:
                sol[i][j] = '+'
                sols.append(sol)
                crosses += 1

    return crosses, sols

def static():        
    c1 = [
        [1,1,1],
        [2,3,1],
        [1,1,1]
    ]
    c2 = [
        [1,1,1],
        [1,3,1],
        [1,1,1]
    ]
    c3 = [
        [4,4,4],
        [5,1,4],
        [0,1,4]
    ]
    c4 = [
        [1,1,1,1],
        [2,3,1,1],
        [1,1,1,0],
        [1,4,1,1]
    ]
    c5 = [
        [2,1,1,1],
        [1,4,1,1],
        [1,1,2,1],
        [1,1,1,1]
    ]
    c6 = [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
    ]
    c7 = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0]] 
    c8 = [
        [1,1,1,1,1],
        [1,5,3,1,1],
        [1,1,1,1,0],
        [4,1,2,1,1],
        [5,3,1,1,1]
    ]
    
    ans, sols = solution(c7)
    print(f'Total # of crosses {ans}')


import random
from pprint import pprint
from tabulate import tabulate

def dynamic():
    mn, mx = 5, 11
    size = random.randint(mn, mx), random.randint(mn, mx)
    
    # a = [[random.choice(vals) for _ in range(size)] for _ in range(size)]
    grid = [[random.randint(0,1) for _ in range(size[0])] for _ in range(size[1])]
    # pprint(a)
    ans, sols = solution(grid)
    return grid, ans, sols

if __name__ == '__main__':
    seed = None #42
    random.seed(seed)
    for i in range(100):
        grid, ans, sols = dynamic()
        if sols:
            print(f"Run: {i} ")
            print('Cross found')
            pprint(grid)
            for sol in sols:
                print(f'{tabulate(sol, tablefmt='plain')}\n')
            print(f'Total number of crosses {ans}\n\n')


    # static()
 

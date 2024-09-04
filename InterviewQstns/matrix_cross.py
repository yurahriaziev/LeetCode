def solution(matrix):
    if len(matrix) == 0:
        return None
    
    rows = len(matrix)
    cols = len(matrix[0])
    crosses = 0

    # sols = []

    for i in range(rows):
        # sol = [[]]
        for j in range(cols):
            nbors = []
            for k in range(1, len(matrix[i])):
                if i - k >= 0:
                    nbors.append(matrix[i-k][j])
                if j + k < len(matrix[i]):
                    nbors.append(matrix[i][j+k])
                if i + k < len(matrix):
                    nbors.append(matrix[i+k][j])
                if j - k >= 0:
                    nbors.append(matrix[i][j-k])
            cross = True
            for num in range(len(nbors)-1):
                if nbors[num] != nbors[num+1]:
                    cross = False

            if cross:
                crosses += 1
                # sols.append(sol)
    return crosses

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
    # TODO: Fix, something's wrong, shows 1
    c7 = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0]]
    
    ans = solution(c7)
    print(ans)


import random
from pprint import pprint

def dynamic():
    mn, mx = 5, 11
    size = random.randint(mn, mx), random.randint(mn, mx)
    
    # vals = ['-', '+']
    # a = [[random.choice(vals) for _ in range(size)] for _ in range(size)]
    a = [[random.randint(0,1) for _ in range(size[0])] for _ in range(size[1])]
    # pprint(a)
    sol = solution(a) # TODO: return array of solutions [[], ]
    # print(sol)
    return a, sol

if __name__ == '__main__':
    seed = None #42
    random.seed(seed)
    for i in range(100):
        a, sol = dynamic()
        if sol:
            print(f"Run: {i} ")
            pprint(a)
            print(sol)

    # static()
 

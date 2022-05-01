def rotate(key):
    row = len(key)
    col = len(key[0])
    rotated = [[0]*row for i in range(col)]
    
    for i in range(row):
        for j in range(col):
            rotated[j][row-i-1] += key[i][j]
    
    return rotated

def solution(key, lock):
    answer = False

    def shift(x, y, row, col):
        shifted = [[0]*col for _ in range(row)]

        krow = len(key)
        kcol = len(key[0])
        for i in range(krow):
            for j in range(kcol):
                if i + x < row and i + x >= 0 and j + y < col and j+ y >= 0:
                    shifted[i+x][j+y] = key[i][j]
        
        for i in range(row):
            for j in range(col):
                if lock[i][j] + shifted[i][j] != 1:
                    return False
        
        return True
    
    for _ in range(4):
        key = rotate(key)
        row = len(lock)
        col = len(lock[0])

        for i in range(-row, row):
            for j in range(-col, col):
                if shift(i, j, row, col):
                    answer = True
                    break

    return answer
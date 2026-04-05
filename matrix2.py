mat1 = [[1,2],[3,4]]
mat2 = [[5,6],[7,8]]

def matrix_check_size(mat1: list,mat2:list) -> bool:
    if (len(mat1) == len(mat2)):
        for i in range(len(mat1)):
            
            if (len(mat1[i]) != len(mat2[i])):
                return False
        else: 
            return True
    else:
        return False

def add_matricies(mat1: list,mat2: list) -> list:
    mat3 = []
    if matrix_check_size(mat1,mat2):
        for i in range(len(mat1)):
            mat3.append([])
            for j in range(len(mat1[0])):
                mat3[i].append(mat1[i][j] + mat2[i][j])
    else:
        print('the matricies are not the same size')
    
    print(mat3)

add_matricies(mat1,mat2)


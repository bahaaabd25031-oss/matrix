import tkinter as tk
class matrix:
    def __init__(self,m : int,n : int):
        self.__rows = m
        self.__cols = n
        self.__size = m*n
        self.__data = []
        for i in range(m):
            self.__data.append([])
            for j in range(n):
                self.__data[i].append(None)
    def get_size(self):
            return self.__size
    def get_rows(self):
            return self.__rows
    def get_cols(self):
            return self.__cols 
    
    @classmethod    
    def Identity(cls,n):
        mat = cls(n,n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    mat.change_mat(1,(i,j))
                else:
                    mat.change_mat(0,(i,j))
        return mat    
                
    def set_mat(self,*values):
        if (type(values[0]) not in [str,set,dict,list,tuple]) and (len(values) == self.__size):
            ctr = 0
            for i in range(self.__rows):
                for j in range(self.__cols):
                    self.__data[i][j] = values[ctr]
                    ctr += 1
        elif (type(values[0]) in [list,tuple])and (len(values[0]) == self.__size):
            ctr = 0
            for i in range(self.__rows):
                for j in range(self.__cols):
                    self.__data[i][j] = values[0][ctr]
                    ctr += 1
        else:
            print('the amount of digits is not sufficient')
                    
    def change_mat(self,value,position = (1,1)):
        row = position[0] - 1
        col = position[1] - 1
        self.__data[row][col] = value
        
    def transpose(self):
        mat = matrix(self.__cols,self.__rows)
        for i in range(self.__rows):
            for j in range(self.__cols):
                mat.change_mat(self.__data[i][j],(j+1,i+1))
        return mat
                
    def determinant(self):
        if sequare_check_size(self):
            if self.__rows == 1:
                return self.__data[0][0]
            if self.__size <= 4:
                a = self.__data[0][0]
                b = self.__data[0][1]
                c = self.__data[1][0]
                d = self.__data[1][1]
                return (a*d)-(b*c)
            else:
                sum = 0
                for k in range(self.__cols):
                    mat = matrix(self.__rows-1,self.__cols-1)
                    x = 0
                    for i in range(1,self.__rows):
                        y = 0
                        for j in range(self.__cols):

                            if j != k:
                                mat.change_mat(self.__data[i][j],(x+1,y+1))
                                y += 1
                        x += 1
                    t = self.__data[0][k]
                    sign = 1 if k % 2 == 0 else -1
                    sum += sign*t* mat.determinant()
                return sum  
        else:
            return 'the matrix is not a sequare'
    def cofactor(self):
        if sequare_check_size(self):
            if self.__size <= 4:
                tmp = matrix(2,2)
                a = self.__data[0][0]
                b = -(self.__data[0][1])
                c = -(self.__data[1][0])
                d = self.__data[1][1]
                tmp.set_mat(d,b,c,a)
                return tmp
            else:
                all_minors = []
                for p in range(self.__rows):
                    for q in range(self.__cols):
                        mat = matrix(self.__rows-1,self.__cols-1)
                        values = []
                        for i in range(self.__rows):
                            for j in range(self.__cols):
                                if (i != p) and (j != q):
                                    values.append(self.__data[i][j])
                        mat.set_mat(values)
                        mat_det = mat.determinant()
                        mat_minor = mat_det*(-1)**(p+q+2)
                        all_minors.append(mat_minor)
                        
                tmp = matrix(self.__rows,self.__cols)
                tmp.set_mat(all_minors)
                return tmp
                        

        else:
            return 'the matrix is not a sequare'
            
    def adjoint(self):
        mat = self.cofactor()
        return mat.transpose() 

    def inverse(self):
        if self.determinant() != 0:
            return self.adjoint()*(1/self.determinant()) 
        else:
            return 'you can\'t make the inverse of this matrix because it has a determinant of 0'          
    
                                   
    def __add__(self: list,other: list) -> list:
        mat = matrix(self.__rows,other.__cols)
        if add_check_size(self,other):
            for i in range(self.__rows):
                for j in range(self.__cols):
                    sum = self.__data[i][j] + other.__data[i][j]
                    mat.change_mat(sum,(i+1,j+1))
            return mat
        else:
            return 'the matricies are not the same size'
    
    def __sub__(self: list,other: list) -> list:
        mat = matrix(self.__rows,other.__cols)
        if add_check_size(self,other):
            for i in range(self.__rows):
                for j in range(self.__cols):
                    sub = self.__data[i][j] - other.__data[i][j]
                    mat.change_mat(sub,(i+1,j+1))
            return mat
        else:
            return 'the matricies are not the same size'
            
    def __mul__(self, other):
        
        if type(other) == int or type(other) == float:
            tmp = matrix(self.__rows,self.__cols)
            for i in range(self.__rows):
                for j in range(self.__cols):
                    tmp.change_mat(self.__data[i][j] * other,(i+1,j+1)) 
            return tmp
        
        else:
            mat = matrix(self.__rows,other.__cols)
            for i in range(self.__rows):
                for j in range(other.__cols):
                    sum = 0
                    for k in range(self.__cols):
                        sum += self.__data[i][k] * other.__data[k][j]
                    mat.change_mat(sum,(i+1,j+1))
            return mat

    def __str__(self):
        s = ""
        for row in self.__data:
            s = s + "|"
            for item in row:
                s += " " + str(item)
            s = s + " |\n"
        return s

def add_check_size(mat1: list,mat2:list) -> bool:
    if (mat1.get_rows() == mat2.get_rows()) and (mat1.get_cols() == mat2.get_cols()):
        return True
    else:
        return False
def sequare_check_size(mat):
    if mat.get_rows() == mat.get_cols():
        return True
    else:
        return False

class matrix_app:
    def __init__(self,root):
        self.root = root
        
        tk.Label(root,text='matrix 1').grid(row=0,column=0) 
        self.mat1_entry = tk.Text(root,width=20,height=4)
        self.mat1_entry.grid(row=0,column=1)
        
        tk.Label(root,text='matrix 2').grid(padx=50,row=1,column=0)
        self.mat2_entry = tk.Text(root,width=20,height=4)
        self.mat2_entry.grid(row=1,column=1)
        
        tk.Button(root,text='add matricies',command=self.add_matrix,height=4,width=15).grid(row=0,column=2)
        tk.Button(root,text='subtract matricies',command=self.sub_matrix,height=4,width=15).grid(row=1,column=2)
        tk.Button(root,text='multplie matricies',command=self.mul_matrix,height=4,width=15).grid(row=0,column=3)
        tk.Button(root,text='find the determinant',command=self.det_matrix,height=4,width=15).grid(row=1,column=3)
        tk.Button(root,text='find the cofactor',command=self.cof_matrix,height=4,width=15).grid(row=0,column=4)
        tk.Button(root,text='find the adjoint',command=self.adj_matrix,height=4,width=15).grid(row=1,column=4)
        tk.Button(root,text='find the transpose',command=self.transpose_matrix,height=4,width=15).grid(row=0,column=5)
        tk.Button(root,text='find the inverse',command=self.inv_matrix,height=4,width=15).grid(row=1,column=5)
        
        self.tmp = tk.Tk()
        self.tmp.geometry('10x10+500+500')
        
    def create_matrix(self,entry):
        rows = entry.get("1.0", "end-1c").split('\n')
        all_values = []
        for row in rows:
            values = row.split(',')
            for value in values:
                all_values.append(int(value))
        mat = matrix(len(rows),len(values))
        mat.set_mat(all_values)
        return mat
    
    def add_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        mat2 = self.create_matrix(self.mat2_entry)
        result = tk.Message(self.tmp,text=mat1+mat2)
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)
        
    def sub_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        mat2 = self.create_matrix(self.mat2_entry)
        result = tk.Message(self.tmp,text=mat1-mat2)
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)
        
    def mul_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        if (',' in self.mat2_entry.get("1.0", "end-1c")):
            mat2 = self.create_matrix(self.mat2_entry)
            result = tk.Message(self.tmp,text=mat1*mat2)
        else:
            mat2 = self.mat2_entry.get("1.0", "end-1c")
            scalar = int(mat2)
            result = tk.Message(self.tmp,text=mat1*scalar)
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)          
    
    def det_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        result = tk.Message(self.tmp,text=mat1.determinant())
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)
        
    def cof_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        result = tk.Message(self.tmp,text=mat1.cofactor())
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)


    def adj_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        result = tk.Message(self.tmp,text=mat1.adjoint())
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)
        
    def transpose_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        result = tk.Message(self.tmp,text=mat1.transpose())
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)
        
    def inv_matrix(self):
        self.tmp.destroy()
        self.tmp = tk.Tk()
        self.tmp.geometry('100x100+500+500')
        mat1 = self.create_matrix(self.mat1_entry)
        result = tk.Message(self.tmp,text=mat1.inverse())
        result.config(bg='white')
        result.grid(padx=10,row=2,column=1)
        
        
    
       
if __name__ == "__main__": 
    root = tk.Tk()
    app = matrix_app(root) 
    root.mainloop()
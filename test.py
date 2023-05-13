import copy

class Test:
    def submatrix(self,A,i,j):
        #矩阵A第i行第j列元素的余矩阵
        p=len(A)#矩阵的行数
        q=len(A[0])#矩阵的列数
        C=[[A[x][y] for y in range(q) if y!=j] for x in range(p) if x!=i]#列表推导式
        return C

    def det(self,A):
        #按第一行展开递归求矩阵的行列式
        p=len(A)#矩阵的行数
        q=len(A[0])#矩阵的列数
        if(p==1 and q==1):
            return A[0][0]
        else:
            value=0
            for j in range(q):
                value+=((-1)**(j+2))*A[0][j]*self.det(self.submatrix(A,0,j))
            return value
        
    def inverse(self,A):
        p=len(A)#矩阵的行数
        q=len(A[0])#矩阵的列数
        C=copy.deepcopy(A)
        d=self.det(A)
        print(d)
        for i in range(p):
            for j in range(q):
                C[i][j]=((-1)**(i+j+2))*self.det(self.submatrix(A,j,i))
                C[i][j]=C[i][j]/d
        print(C)

    def mutiply(self,A,B):
        p=len(A)#矩阵A的行数
        q=len(A[0])#矩阵A的列数=矩阵B的行数
        r=len(B[0])#矩阵B的列数
        C=[[0 for j in range(r)] for i in range(p)]
        for i in range(p):
            for j in range(r):
                for k in range(q):
                    C[i][j]+=A[i][k]*B[k][j]
        return C

    def trans(self,A):
        """
        矩阵转置
        """
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

if __name__ == "__main__":
    test = Test()
    A = [[1,2,3,6],[2,3,4,5],[3,4,5,7]]
    C = test.trans(A)
    print( C.__sizeof__())
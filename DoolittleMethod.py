#region imports
from copy import deepcopy as dcpy
from math import cos,pi
import numericalMethods as nm
import matrixOperations as mo
#endregion

#region Functions
def LUFactorization(A):
    """
    This is the Lower-Upper factorization part of Doolittle's method.  The factorizaiton follows the work in
    Kreyszig section 20.2.  Note: L is the lower triangular matrix with 1's on the diagonal.  U is the upper traingular matrix.
    :param A: a nxn matrix
    :return: a tuple with (L, U)
    """
    n = len(A)
    # Step 1
    U = [([0 for c in range(n)] if not r == 0 else [a for a in A[0]]) for r in range(n)]
    L = [[(1 if c==r else (A[r][0]/U[0][0] if c==0 else 0)) for c in range(n)] for r in range(n)]

    #step 2
    for j in range(1,n):  # j is row index
        #(a)
        for k in range(j,n):  # always j >= 1 (i.e., second row and higher)
            U[j][k]=A[j][k]  # k is column index and scans from column j to n-1
            for s in range(j):  #  s is column index for L and row index for U
                U[j][k] -= L[j][s]*U[s][k]
            #(b)
            for i in range(k+1, n):
                sig=0
                for s in range(k):
                    sig+=L[i][s]*U[s][k]
                L[i][k]=(1/(U[k][k]))*(A[i][k]-sig)
    return (L,U)

def BackSolve(A,b,UT=True):
    """
    This is a backsolving algorithm for a matrix and b vector where A is triangular
    :param A: A triangularized matrix (Upper or Lower)
    :param b: the right hand side of a matrix equation Ax=b
    :param UT: boolean of upper triangular (True) or lower triangular (False)
    :return: the solution vector x, from Ax=b
    """
    nRows=len(b)
    nCols=nRows
    x=[0]*nRows
    if UT:
        for nR in range(nRows-1,-1,-1):
            s=0
            for nC in range(nR+1,nRows):
                s+=A[nR][nC]*x[nC]
            x[nR]=1/A[nR][nR]*(b[nR]-s)
    else:
        for nR in range(nRows):
            s=0
            for nC in range(nR):
                s+=A[nR][nC]*x[nC]
            x[nR]=1/A[nR][nR]*(b[nR]-s)
    B = mo.checkMatrixSoln(A, x, False)
    return x

def Doolittle(Aaug):
    """
    The Doolittle method for solving the matrix equation [A][x]=[b] is:
    Step 1:  Factor [A]=[L][U]
    Step 2:  Solve [L][y]=[b] for [y]
    Step 3:  Solve [U][x]=[y] for [x]
    :param Aaug: the augmented matrix
    :return: the solution vector x
    """
    A,b=mo.separateAugmented(Aaug)
    L,U=LUFactorization(A)
    B=mo.MatrixMultiply(L,U)
    y=BackSolve(L,b, UT=False)
    x=BackSolve(U,y, UT=True)
    return x  #x should be a column vector of form [[], [], [], ..., []]

def main():
    A=[[3, 5, 2],[0,8,2],[6,2,8]]
    L,U=LUFactorization(A)
    print("L:")
    for r in L:
        print(r)

    print("\nU:")
    for r in U:
        print(r)

    aug=[[3,9,6,4.6],[18,48,39,27.2], [9,-27,42,9]]
    aug = [[3, 1, -1, 2],
          [1, 4, 1, 12],
          [2, 1, 2, 10]]
    x=Doolittle(aug)
    x=[round(y,3) for y in x]
    print("x: ", x)
    y=nm.GaussSeidel(aug,[0,0,0])
    y=[round(z,3) for z in y]
    b=mo.checkMatrixSoln(aug,y)
    print("b: ",b)
#endregion

if __name__ == "__main__":
    main()
#region imports
import copy
import math
#endregion

#region functions
def BuildAMatrix(element00, nRows=2, nCols=2):
    '''
    I'm creating a function to build a nRowsXnCols matrix to demonstrate list comprehension.
    Step 1: use a for loop to iterate through the rows of the matrix I want to create.
    Step 2: use a list comprehension to build the values for the columns in each row.  Set odd to negative, even to positive
    :param nRows: number of rows
    :param nCols: number of columns
    :return: a matrix of nRowsXnCols
    '''
    A=[] #empty list called A
    row=[] #a list for temporary storage
    c0=element00
    f=1.0
    y=lambda x,r: x**3+math.sin(x)+r
    for r in range(nRows):
        #row=[(c+c0)*(1.0 if (c+c0)%2==0 else -1.0) for c in range(nCols)]
        row=[y(c,r) for c in range(nCols)]
        # for c in range(nCols):
        #     f=1.0 if (c+c0)%2==0 else -1.0 #ternary operator
        #     row.append(f*(c+c0))
        A.append(row)
        c0+=nCols
    return A

def ElementByElementMult(A,B):
    """
    This multiplies the elements of A by the corresponding elements of B.
    matrices A and B need to be the same size
    :param A: a matrix
    :param B: a matrix
    :return: C as a matrix
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return 'A & B are not the same size'  #encounter problem that matrices are not the same size

    C=[[A[i][j]*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return C
    # for i in range(len(A)):
    #     C.append([])
    #     for j in range(len(A[i])):
    #         C[i].append(A[i][j]*B[i][j])
    # return C

def Main():
    """
    This function should only run for debuggin purposes.  Use a main guard to avoid running it unnecessarily.
    :return: none
    """
    A=BuildAMatrix(1, nRows=10,nCols=10)
    B=BuildAMatrix(10, nRows=10, nCols=10)
    C=ElementByElementMult(A,B)

    A=BuildAMatrix(1, nRows=10,nCols=10)
    B=BuildAMatrix(10, nRows=9, nCols=10)
    C=ElementByElementMult(A,B)
    print(A)
    print(C)
#endregion

if __name__ == "__main__":
    Main()

#Written by Sancheet Hoque
#This module is contains three main functions involving matrices and two assist functions


#Gets the row i of matrix A. Follows python iterations, so row 1 would have a 
#i value of 0
def rowget(A, i):
      row=A[i]
      return row
  
#Gets the column i of matrix A. Follows python iterations, so column 1 would have a 
#i value of 0
def columnget(A, i):
      column = []
      for j in range(len(A)):
           num = A[j][i]
           column.append(num)
      return column



#-----------------------------------------------------------------------------
#1 The Transpose function simply takes any sized matrix and transposes it. 
#The output is the the transposed matrix

def transpose(matrix):
    row=rowget(matrix,0)# gets the row of the matrix
    column=columnget(matrix,0)#gets the column of the matrix
    
    if row==1 and column==1:
        print('Cannot transpose')
    else:    
    #Gets the length number of elements in a row and and iterates them through the matrix replacing
    #them so it's transposed
        transposed = [[j[i] for j in matrix] for i, _ in enumerate(matrix[0])]

        return transposed

#------------------------------------------------------------------------------

#The multmatrix function takes two matrices as input and multiplies them. The output
#is the multiplied matrix


def multmatrix(matrix1,matrix2):
    

    #Checks if the inner dimensions are equal, if not they cannot be multiplied.
    if len (matrix1[0]) != len(matrix2):
        print('These matrices cannot be multiplied')

    else:
        finalmat=[] #list initialization for final answer
        
        #This is the dot product process
        for i in range(len(matrix1)):
            sumlist=[] #list initialization for dot product answers
            
            for k in range(len(matrix1)):
                Arow=rowget(matrix1,i);#getting row i to multiply it by column k
                Bcolumn=columnget(matrix2,k);
                sum1=0
                
                
                for j in range(len(Arow)):
                    sum1+=(Arow[j]*Bcolumn[j]) #dot product adding into one sum
                    
                sumlist.append(sum1) #appends to sum1. the length of this is based on the length of the row
            finalmat.append(sumlist) #appends a row to the final matrix unbtil iterations are done   

        return finalmat


#-----------------------------------------------------------------------------

#The inversemat function calculates the inverse of matrix 
def inversemat(matrix):
    #a function to create an identity matrix given the length of the square matrix
    def identmat(matrix):
        
        ident=[[0 for j in range(matrix)] for i in range(matrix)] #creates an empty matrix with zeros
        #puts in 1s into the same row and columns to create the matrix
        for k in range(0,matrix):
            ident[k][k] = 1
        return ident

    
    
    row=rowget(matrix,0)# gets the row of the matrix
    column=columnget(matrix,0)#gets the column of the matrix
    #checks to see if it's a square matrix
    if len(row) != len(column):
        print("This is not a square matrix, so it can't be inverted")
    else:
        lenmat=range(len(matrix)) #creates an iteration of number of rows
        ident=identmat(len(matrix)) #gets the identity matrix
        
        [matrix[i].append(ident[i][j]) for i in lenmat for j in lenmat] #appends the identity matrix to the input matrix
        
        #normalizing process
        for i in lenmat:
            piv = float(matrix[i][i])#pivot
            #diving values by the pivot
            for j in range(len(matrix[i])):
                matrix[i][j] = float(matrix[i][j])/piv        
            
                
        for i in lenmat:
           
            
            iter1=[n for n in lenmat if lenmat[n] !=i] #getting iterations depending on if row n thats not row i 
    
                    
            for j in iter1:
                x = matrix[j][i]/matrix[i][i]#finds the ratio Aji/Aii; A = matrix
                for k in range(len(matrix[j])):
                    matrix[j][k]-=x*matrix[i][k] #subtract x*Ai from Aj           
                
        #final step in normalizing        
        for i in lenmat:            
            calc=matrix[i][i]  #pivot      
            for l in range(len(matrix[i])):
                matrix[i][l] = round(matrix[i][l]/calc,3) #rounding the final values. Left side should be identity matrix now
                
        #receives the inverse from the orignal matrix       
        inverse=[matrix[i][len(matrix):len(matrix[i])] for i in lenmat]
        
        if len(str(inverse[0])) > 12 :
            print('The determinant is zero, so it does not have inverse')
            
        
        return inverse

    

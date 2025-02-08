NUM_RMDS = 9   # number of right-most digits required

def multiply2by2(A, B):
    """Takes two 2-by-2 matrices, A and B, and returns their product. The
    product will only contain a limited number of digits to cope with
    large numbers.  The input and output matrices are in the form of
    lists of lists (of lengths 2). This function only works for 2-by-2
    matrices. The size (dimensions) of the input does not grow with
    respect to n in the original problem. Therefore the time
    complexity of this function is Theta(1). This is different from
    the general matrix multiplication problem where the time
    complexity for multiplying two n-by-n matrices is O(n^3).

    """

    # compute the matrix product
    product = [
        [A[0][0]*B[0][0]+A[0][1]*B[1][0],	A[0][0]*B[0][1]+A[0][1]*B[1][1]],	 
        [A[1][0]*B[0][0]+A[1][1]*B[1][0],	A[1][0]*B[0][1]+A[1][1]*B[1][1]]
        ]
    
    # retain only the required number of digits on the right
    product = [[x % 10**NUM_RMDS for x in row] for row in product]
    
    return product

def matrix_power(A, n):
    """Takes a 2x2 matrix A and a non-negative integer n as exponent and
    returns A raised to the power of n (which will be a 2x2 matrix)."""
    
    # if n is 0 then return the identity matrix.
    if n == 0:
        return [[1, 0],
                [0, 1]]
    
    # Complete the rest
    

def fib(n):
    """Returns the n-th Fibonacci number by raising a special matrix to the
    power of n and returning an element on the off-diagonal."""
    
    A = [[1, 1], 
         [1, 0]]
         
    return matrix_power(A, n)[0][1]

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(100))
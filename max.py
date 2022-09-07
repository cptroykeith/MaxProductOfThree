def solution(A):

    A.sort()

    N=len(A)

    p1= A[N-1]*A[0]*A[1]
    p2= A[N-1]*A[N-2]*A[N-3]
    
    return max(p1,p2)
    
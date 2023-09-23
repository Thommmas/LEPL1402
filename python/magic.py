"""
     * A magic square is an (n x n) matrix such that:
     *
     * - all the positive numbers 1,2, ..., n*n are present (thus each number appears exactly once)
     * - the sums of the numbers in each row, each column and both main diagonals are the same
     *
     *   For instance a 3 x 3 magic square is the following
     *
     *   2 7 6
     *   9 5 1
     *   4 3 8
     *
     *   You have to implement the method that verifies if a matrix is a valid magic square
     */

    /**
     *
     * @param matrix a square matrix of size n x n
     * @return true if matrix is a n x n magic square, false otherwise
     """

def is_magic(m):
    if len(m[0]) != len(m):
        return False
    sum_diags = 0
    for n in range(len(m)):
        #print(n,len(m),m[n])
        sum_diags += m[n][n] + m[n][len(m)-n-1]

        if n != 0 :
            pre_sum  = sum_line
        sum_line = 0
        #print(n,' ',sum_line)
        for i in m[n]:
            sum_line += i
        if (n >= 1) and (not sum_line == pre_sum):
            #print(n,'== 0 and ', sum_line)
            return False
    if (sum_diags // 2) != sum_line :
        #print(sum_diags//2,'==',sum_line)
        return False
    return True


#tests 

print(is_magic(((2,7,6),(9,5,1),(4,3,8))))
print(is_magic(((2,7,6),(9,5,1),(4,3,1))))
print(is_magic(((9,3,22,16,15),(2,21,20,14,8),(25,19,13,7,1),(18,12,6,5,24),(11,10,4,23,17))))
'''
  9   3  22  16  15
  2  21  20  14   8
 25  19  13   7   1
 18  12   6   5  24
 11  10   4  23  17
 '''
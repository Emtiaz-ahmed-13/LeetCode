# 1.iteration over the possible colum pairs:
#     need two nested loops (i,j)
#     sum of elements in the submatrix between those columns for each row.
# 2. count the submatrixcs with the target sum
#     for each submatrix count the occurences of cumulative sums
#     it use the var cur to represent the current sum of element in the submatrix
#     if cur-target has been encountered before,if so it increments the res by count of 
#     occurrence stored in c[curr-target]
#     the counter c is then updated to reflect the occurrence of the current cummulative sum
# 3. return result :
#     the final res represent the count of submaxtrices whose sum meet the target.
#--------------------------------------------------------------------------------------------------------
# T.C: O(n^2 * m) where n is the number of columns and m is the number of rows.
# S.C: O(m). where m is the number of rows.

from typing import Collection, List


class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        # Get the dimensions of the matrix
        m, n = len(A), len(A[0])

        # cumulative sum for each row
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]

        res = 0  # Initialize the result 

        # Iterate over all possible pairs of columns
        for i in range(n):
            for j in range(i, n):
                c = Collection.defaultdict(int)
                cur, c[0] = 0, 1  # Initialize the current sum and a counter for cumulative sums

                # Iterate over each row to calculate the submatrix sum
                for k in range(m):
                    # Update the current sum based on the cumulative row sums
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)

                    # Count submatrices with the target sum using cumulative sums
                    res += c[cur - target]

                    # Update the counter for the current cumulative sum
                    c[cur] += 1

        return res
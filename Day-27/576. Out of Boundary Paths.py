# Problem Link:
#     https://leetcode.com/problems/out-of-boundary-paths/?envType=daily-question&envId=2024-01-26

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        # Create a memoization grid to store intermediate results
        memo = {}
        
        def count(x, y, moves):
            # If the move is out of bounds, return 1 (path found)
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            # If we've reached maximum moves, return 0 (no path)
            if moves == maxMove:
                return 0
            # Check if result is already computed for current position and moves
            cached_result = memo.get((x, y, moves))
            if cached_result is not None:
                return cached_result

            # Calculate the total paths by exploring all four directions
            total = 0
            total += count(x + 1, y, moves + 1)
            total += count(x, y + 1, moves + 1)
            total += count(x - 1, y, moves + 1)
            total += count(x, y - 1, moves + 1)
            
            # Store the result in memoization grid
            memo[(x, y, moves)] = total % MOD
            return memo[(x, y, moves)]

        # Start the recursion from the given start position with 0 moves
        return count(startRow, startColumn, 0)

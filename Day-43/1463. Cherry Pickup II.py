#PROBELM LINK:
    #https://leetcode.com/problems/cherry-pickup-ii/description/?envType=daily-question&envId=2024-02-11
    
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def maxfinder(x1, y1, x2, y2):
            m, n = len(grid), len(grid[0])

            # Return the sum of no: of cherries of the current grids of the robots 
            # if the robots have reached the last row (it can't move further).
            if x1 == m - 1 and x2 == m - 1:
                return grid[x1][y1] + grid[x2][y2]

            # Find the next possible y-coordinates of both robots.
            y1_possible = [y1]
            if y1 > 0:
                y1_possible.append(y1 - 1)
            if y1 < n - 1:
                y1_possible.append(y1 + 1)

            y2_possible = [y2]
            if y2 > 0:
                y2_possible.append(y2 - 1)
            if y2 < n - 1:
                y2_possible.append(y2 + 1)

            # Try all combinations of the next y-coordinate of both robots. 
            # Since each robot can have at most 3 possible next y-coordinates, 
            # maximum of 3*3=9 combinations are possible.
            result = -float('inf')
            for y1_poss in y1_possible:
                for y2_poss in y2_possible:
                    if y1_poss < y2_poss:
                        # Calculate the cherries that can be picked for each of these combinations,
                        # and return the max value
                        result = max(result, grid[x1][y1] + grid[x2][y2] + maxfinder(x1 + 1, y1_poss, x2 + 1, y2_poss))
            return result

        return maxfinder(0, 0, 0, len(grid[0]) - 1)

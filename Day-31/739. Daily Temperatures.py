# Intuition
# A stack is ideal for this scenario because we are dealing with an order of elements (days) where the most recently seen temperatures are more relevant for comparison. The stack will store indices of days in a way that maintains the temperatures in a non-increasing order from top to bottom. This way, when we encounter a warmer temperature, we know that it is warmer than all the temperatures represented by indices currently on the stack.

# Approach: 
# Initialization: We start by initializing an array answer filled with zeros, with the same length as the input temperatures array. This array will store the number of days until a warmer temperature is found for each day. We also initialize an empty stack that will store indices from the temperatures array.

# Iterating Through Temperatures: We iterate through each temperature in the temperatures array. For each day's temperature, we check the stack to see if we can find any days that have been waiting for a warmer temperature.

# Updating Answer and Managing Stack:

# As long as the stack is not empty and the current day's temperature is higher than the temperature of the day at the top of the stack, we pop the stack. The difference between the current day's index and the popped index gives us the number of days until a warmer temperature for that day. We update this in the answer array.
# We then push the current day's index onto the stack. This is done for every day, ensuring that the stack always contains days waiting for a warmer temperature.
# Final Result: Once we've processed all days, the answer array contains, for each day, the number of days one would have to wait to experience a warmer temperature. If no warmer temperature is found in the future, the value remains zero as initialized.

# Complexity
# Time complexity: O(n)

# Space complexity:O(n)

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)

        return answer
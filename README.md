# Leetcode
1491. Average Salary Excluding the Minimum and Maximum Salary 

**Logic**
1. Initialize variables a and b to store the maximum and minimum salaries, respectively. Use the max and min functions to find these values.
2. Create an empty list x to store the salaries excluding the minimum and maximum salaries.
3. Iterate over the range of indices in the salary list using a for loop.
4. Check if the current salary at index i is not equal to a (maximum salary) and not equal to b (minimum salary).
5. If the condition is true, append the current salary to the x list.
6. After the loop, get the length of the x list and assign it to variable y.
7. Calculate the sum of the salaries in the x list using the sum function, and divide it by y to get the average.
8. Return the average as the result.

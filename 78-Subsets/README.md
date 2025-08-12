Given an integer array nums of unique elements, return all possible subsets (the power set).
- all solutions/ all subsets
- binary tree of choices

<img width="600" height="249" alt="image" src="https://github.com/user-attachments/assets/2c3f8aa8-9bed-4d7c-9fd0-26e203db6d16" />

1. make decision 
2. recurse
3. base case
4. undo decision
The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


Example 2:

Input: nums = [0]
Output: [[],[0]]


 
Constraints:


	1 <= nums.length <= 10
	-10 <= nums[i] <= 10
	All the numbers of nums are unique.


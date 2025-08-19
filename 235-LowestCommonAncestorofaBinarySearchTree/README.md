Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

<img width="215" height="208" alt="Screenshot 2025-08-19 at 1 58 21 PM" src="https://github.com/user-attachments/assets/0d38eddc-3c81-4bed-8b3c-da2a628d4635" />

 
Example 1:

<img width="436" height="302" alt="image" src="https://github.com/user-attachments/assets/faf8708b-eda5-44bf-90fc-8f3cc2b2903c" />


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


 
Constraints:


	The number of nodes in the tree is in the range [2, 105].
	-109 <= Node.val <= 109
	All Node.val are unique.
	p != q
	p and q will exist in the BST.


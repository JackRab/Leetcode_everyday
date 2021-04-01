"""
Link: https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        The idea is to compare values from each node every time and append the node with minimum value
        to the merged list
        """
        """
        Time complexity: O(N*logN), where N is the total number of nodes since sort list takes Nlogn time
        Space complexity: O(N) to store res
        """
        self.nodes = []
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        head = point = ListNode()
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next

if __name__ == '__main__':
    # [[1,4,5],[1,3,4],[2,6]]
    node1 = ListNode(1)
    node1.next = ListNode(4)
    node1.next.next = ListNode(5)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    node3 = ListNode(2)
    node3.next = ListNode(6)

    Solution().mergeKLists([node1, node2, node3])
    

# merge k sorted lists          
#class Solution:
#    def mergeKLists(self, lists: List[List]) -> List:
#        """
#        The idea is to compare values from each node every time and append the node with minimum value
#        to the merged list
#        """
#        """
#        Time complexity: O(N*n), where N is the total number of nodes, n is the number of list
#        Space complexity: O(N) to store res
#        """
#        n = len(lists)
#        if n == 0:
#            return []
#        
#        index = [0]*n
#        lengths = [len(lists[i]) for i in range(n)]
#        res = []
#        while any([index[i] < lengths[i] for i in range(n)]):
#            min = float('inf')
#            i_pop = 0
#            for i in range(n):
#                if index[i] < lengths[i]:
#                    # this list has not reached the end
#                    if lists[i][index[i]] <= min:
#                        i_pop = i
#                        min = lists[i][index[i]]
#
#            res.append(lists[i_pop][index[i_pop]])
#            index[i_pop] += 1
#
#        return res
#
#if __name__ == '__main__':
#    assert Solution().mergeKLists([[1,4,5],[1,3,4],[2,6]]) == [1,1,2,3,4,4,5,6]
#    assert Solution().mergeKLists([]) == []
#    assert Solution().mergeKLists([[]]) == []
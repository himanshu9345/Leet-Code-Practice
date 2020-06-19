class Node:
    def __init__(self, val):
        super().__init__()
        self.char = val
        self.child = []

class Solution:
    def __init__(self, nums, times):
        super().__init__()
        print(nums, times)
    def input(self, char):
        print(char)

nums = ["i love you", "island","ironman", "i love leetcode"]
times = [5,3,2,2]
sol = Solution(nums, times)
sol.input("a")
class Solution(object):
    def connect(self, root1):
        if not root1:
            return None
        queue = collections.deque([root1])
        nextlevel = collections.deque()
        
        while queue:
            root = queue.popleft()
            if root.left:
                nextlevel.append(root.left)
            if root.right:
                nextlevel.append(root.right)
            if queue:
                root.next = queue[0]
            if not queue:
                queue, nextlevel = nextlevel,queue
        return root1
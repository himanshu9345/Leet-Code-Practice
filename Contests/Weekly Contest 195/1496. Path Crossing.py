class Solution(object):
    def isPathCrossing(self, path):
        i = 0
        start  = (0,0)
        seen = set([start])
        while i < len(path):
            if path[i] == "N":
                start = (start[0],start[1]+1)
            elif path[i] == "S":
                start = (start[0],start[1]-1)
            elif path[i] == "E":
                start = (start[0]+1,start[1])
            elif path[i] == "W":
                start = (start[0]-1,start[1])
            if start in seen:
                return True
            
            seen.add(start)
            i += 1
        return False
        """
        :type path: str
        :rtype: bool
        """
        
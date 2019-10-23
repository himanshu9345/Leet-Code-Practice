def check(a, b, x1, y1, x, y):
    if (x1 - x) * b == (y1 - y) * a:
        return True
    return False


class Solution(object):
    def checkStraightLine(self, coordinates):
        # m=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        x1 = (coordinates[1][0] - coordinates[0][0])
        y1 = (coordinates[1][1] - coordinates[0][1])
        for i in range(2, len(coordinates)):
            if not check(x1, y1, coordinates[i][0], coordinates[i][1], coordinates[0][0], coordinates[0][1]):
                return False
        return True
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

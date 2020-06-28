class Solution(object):
    def average(self, salary):
        return (sum(salary)-min(salary)-max(salary)+0.0)/(len(salary)-2)
        """
        :type salary: List[int]
        :rtype: float
        """
        
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count =0
        for i in range(len(startTime)):
            if queryTime in [k for k in range(startTime[i],endTime[i]+1)]:
                count+=1
        return count
            
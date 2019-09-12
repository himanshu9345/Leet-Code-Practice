from collections import deque


def bfs(start, end, seen, deadends):
    q = []
    q.append(start)
    count = 0
    while (q):
        count += 1
        # print q
        new1 = []
        for i in range(len(q)):
            comb = q[i]
            if comb not in seen:
                seen.add(comb)
                if comb == end:
                    # print comb
                    return count - 1
                for i in range(4):
                    new_s = comb[0:i] + str((int(comb[i]) + 1) % 10) + comb[i + 1:]
                    new_rs = comb[0:i] + str((int(comb[i]) + 9) % 10) + comb[i + 1:]

                    # if new_s=="0203" or new_rs=="0203":
                    # print comb,count
                    if new_rs not in seen:
                        # seen.add(new_rs)
                        new1.append(new_rs)
                    if new_s not in seen:
                        # seen.add(new_s)
                        new1.append(new_s)
        q = new1

        # print q
    return -1


class Solution(object):
    def openLock(self, deadends, target):
        if target in deadends:
            return -1
        deadends = set(deadends)
        seen = set(deadends)
        # seen.add("0000")
        end = target
        # print seen
        count = bfs("0000", end, seen, deadends)
        return count

        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

#Dijkstra's Algorithm  70%
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dict1 = defaultdict(list)
        
        for i, j, k in times:
            dict1[i-1].append((j-1,k))
            # heapq.heappush(heap, (k,i-1,j-1))
        heap = [(0, K-1)]
        # for i  in dict1[K-1]:
        #     # visited[i[0]] = True
        #     heapq.heappush(heap, (i[0], i[1]))
        #     time = max(time, i[1])
        # if all(visited):
            # return time
        dict2 = {}
        while heap:
            # print heap
            w, i = heapq.heappop(heap)
            if i in dict2:
                continue
            dict2[i] = w
            # if i not in dict2:
            #     dict2[i] = w
            # else:
            #     continue
            # # visited[i] = True
            # if all(visited):
                # time = w
                # return time
            for node, nw in dict1[i]:
                if node not in dict2:
                    heapq.heappush(heap, (w + nw, node))
                    # visited[node] = True
            
            # if all(visited):
                # time = ma(time, w)
        # print dict2,visited
        if len(dict2) == N:
            return max(dict2.values())
        return -1


class Solution(object): # 5%
    def networkDelayTime(self, times, N, K):
        dict1 = defaultdict(list)
        for i, j, k in times:
            dict1[i-1].append((j-1,k))
        
        dist = {}
        def dfs(node, time):
            if node in dist and dist[node] <= time:
                return
            dist[node] = time
            for i, w in dict1[node]:
                dfs(i, time + w)
        
        dfs(K-1, 0)
        if len(dist) == N:
            return max(dist.values())
        return -1

class Solution(object):# dijkastra 74%
    def networkDelayTime(self, times, N, K):
        dict1 = defaultdict(list)
        for i, j, k in times:
            dict1[i-1].append((j-1,k))
        
        dist = [float('inf')] * N
        visited = [False] * N
        dist[K-1] = 0
        while True:
            curr_node = -1
            curr_dist = float('inf')
            for i in range(N):
                if not visited[i] and dist[i] < curr_dist:
                    curr_node = i
                    curr_dist = dist[i]
            # print curr_node, dist, curr_dist
            if curr_node == -1: break
            
            for j, w in dict1[curr_node]:
                dist[j] = min(dist[j], curr_dist + w)
            visited[curr_node] = True
        # print dist
        if all(visited):
            return max(dist)
        return -1
        # if len(dist) == N:
            # return max(dist.values())
        # return -.1
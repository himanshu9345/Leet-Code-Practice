class Solution(object):
    def twoCitySchedCost(self, costs):
        costs = sorted(costs, key = lambda a : a[0] - a[1])
        return sum([cost[0] for cost in costs[:(len(costs)/2)]]) +  sum([cost[1] for cost in costs[(len(costs)/2):]])
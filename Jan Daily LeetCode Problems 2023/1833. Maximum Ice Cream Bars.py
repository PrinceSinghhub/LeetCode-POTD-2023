class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        if min(costs) > coins:
            return 0

        costs.sort()
        count = 0
        for i in costs:
            if i <= coins:
                coins -= i
        return count

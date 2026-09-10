def CanShip(weights,days_have,capacity):
    current_weight = 0
    days_needed = 1

    for i in weights:
        if current_weight + i <= capacity:
            current_weight += i
        else:
            days_needed += 1
            current_weight = i

    return days_needed <= days_have
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low+high) // 2
            if CanShip(weights,days,mid):
                high = mid
            else :
                low = mid + 1
        return low
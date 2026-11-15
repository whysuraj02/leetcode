class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n-1
        boat = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1
            boat += 1
        return boat
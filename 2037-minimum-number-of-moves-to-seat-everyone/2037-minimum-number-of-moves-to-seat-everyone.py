class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        tot_move = 0
        i = 0
        n = len(seats)
        while i < n:
            if seats[i] == students[i]:
                i += 1
                continue
            else:
                move = abs(students[i] - seats[i])
                tot_move += move
                i += 1
        return tot_move
        




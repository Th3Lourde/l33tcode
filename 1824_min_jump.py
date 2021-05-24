

class Solution:
    def minSideJumps(self, obstacles):
        jumps = [1,0,1]

        for o in obstacles:
            if o:
                jumps[o-1] = float('inf')

            for lane in range(3):
                if lane != o-1:
                    jumps[lane] = min(jumps[lane], jumps[(lane+1)%3]+1, jumps[(lane+2)%3]+1)

        return min(jumps)

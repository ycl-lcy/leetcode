import itertools

class Solution(object):

    def combinationSum(self, candidates, target):
        sols = []
        self.solve(0, [], candidates, target, sols)
        sols.sort()
        sols = list(sols for sols,_ in itertools.groupby(sols))
        return sols       
    
    def solve(self, x, sol, cand, t, sols):
        for ii,i in enumerate(cand):
            sol.append(i)
            x += i
            if x < t:
                x, sol = self.solve(x, sol, cand, t, sols)
                x -= sol[-1]
                sol.pop()
                continue
            if x >= t:
                if x == t:
                    sols.append(sorted(sol))
                x -= sol[-1]
                sol.pop()
                if ii == len(cand)-1:
                    return x, sol
                continue
        return x, sol

#if __name__ == '__main__':
#    s = Solution()
#    print s.combinationSum([8,7,4,3], 11)


import itertools

with open("input", "r") as f:
    s = f.read()
    s = s[:-1]
i = s.find("[")+1
p = int(s[s.find("]")+2])
cand = []
while(s[i] != "\n"):
    cand.append(int(s[i]))
    i += 2
sols = []
def solve(x, sol):
    for ii,i in enumerate(cand):
        sol.append(i)
        x += i
        if x < p:
            x, sol = solve(x, sol)
            x -= sol[-1]
            sol.pop()
            continue
        if x >= p:
            if x == p:
                sols.append(sorted(sol))
            x -= sol[-1]
            sol.pop()
            if ii == len(cand)-1:
                return x, sol
            continue
    return x, sol
solve(0, [])
sols.sort()
sols = list(sols for sols,_ in itertools.groupby(sols))
print("[", end="")
s = ""
for sol in sols:
    s += "["
    for i in sol:
        s += str(i)
        s += ","
    s = s[:-1]
    s += "],"
s = s[:-1]
print(s, end="")
print("]", end="")

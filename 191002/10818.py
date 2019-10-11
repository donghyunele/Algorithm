# 내코드
import sys

inp = sys.stdin.readline

n = int(inp().strip())

max = -1000001
min = 1000001

x = map(int, inp().split(' '))
print(min, max)

# 숏코드
import sys

inp = sys.stdin.readline
n = int(inp().strip())
*_, = map(int, inp().split(' '))

print(min(_), max(_))
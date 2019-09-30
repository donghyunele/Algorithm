import sys

inp = sys.stdin.readline

T = int(inp())

for t in range(T):
  A, B = map(int, inp().split())
  print('Case #{}: {} + {} = {}'.format(t+1, A, B, A+B))
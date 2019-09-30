import sys

inp = sys.stdin.readline

k = int(inp())

for s in range(1, k+1):
  a, b = inp().split(' ')
  num = int(a) + int(b)
  print('Case #%d: %d' % (s,num))

  # 숏코딩 #1
  for n in range(int(input())):print(f"Case #{n+1}: {sum(map(int,input().split()))}")

  # 숏코딩 #2
  T = int(input())
  
  for t in range(T):
    A, B = map(int, input().split())
    print('Case #{}: {}'.format(t+1, A+B))
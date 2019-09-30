import sys

inp = sys.stdin.readline

num = int(inp())

for i in range(1, num+1):
  for j in range(1, i+1):
    print('*', end='')
  print('')
import sys

inp = sys.stdin.readline

while(True):
  a, b = map(int, inp().split())
  if(a==0 & b==0):
    break
  print(a+b)
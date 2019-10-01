import sys

inp = sys.stdin.readline

while(True):
  try:
    a, b = map(int, inp().split())
    print(a+b)
  except Exception:
    break
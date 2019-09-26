A = input()
B = input()

for a in ''.join(reversed(B)):
  print(int(a) * int(A))

print(int(A) * int(B))
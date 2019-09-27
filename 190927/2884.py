in_data = input().split(' ')

m = int(in_data[0])
s = int(in_data[1])

s = s - 45

if s<0:
  m = m-1
  s = s+60

  if m < 0:
    m = m + 24

print(m, s)
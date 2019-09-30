in_data = input().split(' ')
val = input().split(' ')

for i in range(0, int(in_data[0])):
  if int(val[i]) < int(in_data[1]):
    print(val[i])
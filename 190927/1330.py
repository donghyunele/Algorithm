# 첫째 줄에 다음 세 가지 중 하나를 출력한다.

# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.

in_data = input().split(' ')

if int(in_data[0]) > int(in_data[1]):
  print ('>')
elif int(in_data[0]) < int(in_data[1]):
  print ('<')
else:
  print ('==')
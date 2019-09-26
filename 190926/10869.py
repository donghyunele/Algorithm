# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

input_data = input().split(' ')

print(int(input_data[0]) + int(input_data[1]))
print(int(input_data[0]) - int(input_data[1]))
print(int(input_data[0]) * int(input_data[1]))
print(int(int(input_data[0]) / int(input_data[1])))
print(int(input_data[0]) % int(input_data[1]))
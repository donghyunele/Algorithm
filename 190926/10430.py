input_data = input().split(' ')

print((int(input_data[0]) + int(input_data[1])) % int(input_data[2]))
print((int(input_data[0]) % int(input_data[2]) + int(input_data[1]) % int(input_data[2])) % int(input_data[2]))
print((int(input_data[0]) * int(input_data[1])) % int(input_data[2]))
print((int(input_data[0]) % int(input_data[2]) * int(input_data[1]) % int(input_data[2])) % int(input_data[2]))
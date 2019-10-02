import sys

inp = sys.stdin.readline

fir_num = int(inp().strip())
sec_num = 0
res_num = 0
cnt = 1

if not (0 <= fir_num <= 99):
  exit()

num_chk = fir_num

while True:
  sec_num = fir_num % 10
  fir_num = fir_num // 10
  res_num = fir_num + sec_num
  fir_num = (sec_num * 10) + res_num % 10

  if(num_chk == fir_num):
    break
  else:
    cnt += 1

print(cnt)
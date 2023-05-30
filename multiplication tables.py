# 九九を1の段から9の段まで表示

first_number = 1
second_number = 1

while first_number < 10:
  # 掛け算
  multipl = print(str(first_number) + "*" + str(second_number) + "=" + str(first_number * second_number))
  # 2番目の数字が9以外の場合
  if second_number != 9:
    multipl
    second_number += 1
  #2番目の数字が9の場合
  else:
    multipl
    first_number += 1
    second_number -= 8
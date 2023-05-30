# 10個の数字を入力し、最後に入力した数字を入力した回数を表示

max = 10
numbers = []

while max > 0:
  numbers.append(input("数字を入力してください"))
  max -= 1

count = 0
for i in numbers:
  if i == numbers[8]:
    count += 1

# 10個すべて同じ数字の場合
if count == 10:
  print("perfect!!")
else:
  print(str(numbers[8]) + "が出てきた回数は" + str(count) + "回です")

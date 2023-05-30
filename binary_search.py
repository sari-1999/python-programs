# リストの中に入力した値が存在するかを調べる

numbers = [0, 1, 5, 7, 9, 11, 15, 20, 24]

def binary_search (nums, num):
  index = 0
  in_nums = False
  for i in nums:
    if i == num:
      print(str(input_num) + "はリストの中に入っています")
      in_nums = True
      break
    else:
      index += 1
  if in_nums == False:
    print(str(input_num) + "はリストの中に入っていません")

input_num = int(input("好きな数字を入力してください"))
binary_search(numbers, input_num)
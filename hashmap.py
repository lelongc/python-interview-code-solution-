def twoSum(nums, target):
  hashmap = {} # khởi tạo 1 hashmap rỗng 
  for i, num in enumerate(nums): # duyệt qua từng phần tử của mảng với num là giá trị và i là chỉ số 
    complement = target - num # ví dụ target = 9 thì tìm số 2 lấy 9-2 bằng 7 
    if complement in hashmap: # thấy 7 chưa có trong hashmap nó đẩy 2 vô hashmap 
      return [hashmap[complement], i] # khi đến số 7 nó thấy 9-7 = 2 mà 2 đã có trong hashmap nên nó sẽ return về chỉ số của tk đã trong hashmap (tk ở trước là số 2 ) và thằng ở sau (tk hiện tại đang xét là số 7  )
    hashmap[num] = i
  return None

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
if result:
  print(f"Hai chỉ số là: {result}")
else:
  print("Không tìm thấy hai số thỏa mãn yêu cầu.")

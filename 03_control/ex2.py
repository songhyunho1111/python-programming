# 반복문 : while문, for문

# while문
# 1~10까지의 반복 출력
i = 1
while i < 11:   #<-이 조건문이 false가 될때 else
    print(i)
    i+=1
    if i == 8:
        break
else:
    print("End")

nums = [1,3,5,7,9]
target = 2
i = 0

while i<len(nums):
    if nums[i] == target:
        print(f"{target} found.")
        # found = True
        break
    i += 1
else: 
    print(f"{target} not found.")

# if not found:
#     print(f"{target} not found")

# 1 ~ 10까지의 합
i = 1
tot = 0

while i<11:
    i+=1
    if i%2 == 1 :
        continue
    tot += i
else: 
    print(f"sum : {tot}")
    
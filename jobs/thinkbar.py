'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
'''
people = [1, 1, 2, 2, 3]
limit = 5
people.sort()  # [1, 1, 2, 2, 3]
i, j = 0, len(people) - 1
boats = 0

while i <= j:
    if people[i] + people[j] <= limit:
        i += 1
    j -= 1
    boats += 1

print(f'you need {boats} boats')

#  pause_stop

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
nums = [8, 2, 5, 7, 8, 4, 6]
target = 12

seen = {}
result = []

for i, num in enumerate(nums):
    diff = target - num
    if diff in seen :
        result = [seen[diff], i]
        break
    seen[num] = i

print('result : ', result)

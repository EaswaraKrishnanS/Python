import random
lottery_nums = []

for x in range(100) :
    lottery_nums.append(random.randint(1000,9999))

print(len(lottery_nums))
#print(lottery_nums)

lucky_person = random.sample(lottery_nums,2)

print(lucky_person)
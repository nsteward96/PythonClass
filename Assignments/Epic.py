def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    
def userString(prompt):
    print prompt,
    string = raw_input()
    return string
    
def kmToMi(km):
    return 0.62 * km
    
def calcAveNum(nums, start, stop):
    sum = 0.0
    for i in range(start, stop):
        sum += nums[i]
    return sum / (start - stop)
def userList(prompt):
    print prompt,
    l = raw_input().split(",")
    return l

def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    
def userString(prompt):
    print prompt,
    string = raw_input()
    return string

def user2OptionsString(prompt, option1, option2):
    userChoice = ""
    while userChoice != option1 and userChoice != option2:
        userChoice = str.upper(userString(prompt))
    if userChoice == option1:
        return option1
    return option2
    
def kmToMi(km):
    return 0.62 * km
    
def calcAveNum(nums, start, stop):
    sum = 0.0
    for i in range(start, stop):
        sum += nums[i]
    return sum / (start - stop)

def promptUserRunAgain(prompt):
    userResponse = ""
    while userResponse != "Y" and userResponse != "N":
        userResponse = str.upper(userString(prompt))
    if userResponse == "N":
        return False
    return True
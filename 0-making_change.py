def makeChange(coins, total):
    if total < 0:
        return 0
    
    # Initialize a list to store minimum coins needed for each amount up to total
check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
